from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from .forms import RegistrationForm, ProfileForm, NewsForm, ComentForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LogoutView, LoginView
from .models import User, Profile, News
from django.core.paginator import Paginator


# Класс отображения главной страницы.
class MainListView(ListView):
    model = News
    template_name = "app_users/index.html"
    context_object_name = "news"

    def get(self, request):
        key = request.GET.get("search", "")
        if key:
            news = News.objects.filter(title__icontains=key)
        else:
            news = News.objects.all()

        paginator = Paginator(news, 5)

        page = request.GET.get("page")
        page_obj = paginator.get_page(page)

        return render(request, self.template_name, {"page_obj": page_obj})

    class Meta:
        ordering = ["-created"]


# класс отвечающий за отображение страницы деталей новости.
class NewsDetailView(FormMixin, DetailView):
    template_name = "app_users/news_detail.html"

    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        if request:
            form = ComentForm
            return render(request, self.template_name , context={"news": news, "form": form, "pk": pk})

    def post(self, request, pk):
        if request.user.is_authenticated:
            form = ComentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user_name = request.user
                comment.news_id = pk
                comment.save()
        else:
            form = ComentForm(request.POST)
            if form.is_valid():
            # Здесь передаём после проверки атрибутам формы значения и после сохраняем форму!!
                comment = form.save(commit=False)
                comment.user_name = "Аноним"
                comment.news_id = pk
                comment.save()
                return HttpResponseRedirect("?")
        return render(request, "app_users/news_detail.html", context={"form": form})


# Класс регистрации новых пользователей.
class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, "app_users/registration.html", context={"form": form})



    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            u_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=u_password)
            login(request, user)
            return redirect("/")
        else:
            form = RegistrationForm()
        return render(request, "app_users/registration.html", {"form": form})


# Класс управляющий выходом из акаунта.
class OutView(LogoutView):
    next_page = "/"

# Класс управляющий авторизацией пользователей.
class AuthView(LoginView):
    template_name = "app_users/login.html"

# Класс управляющий личным кабинетом юзера.
class ProfileView(View):
    template_name = "app_users/profile.html"

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user_list = User.objects.all()
        if request.user.is_authenticated:
            return render(request, "app_users/profile.html", context={"user": user, "user_list": user_list,  "pk": pk})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user_list = User.objects.all()
        if request:
            data = request.POST.get("data")
            curr_user = User.objects.get(pk=data)
            print(data, curr_user, curr_user.profile.verify)
            if curr_user.profile.verify == False:
                curr_user.profile.verify = True
                curr_user.save()
            else:
                curr_user.profile.verify = False
                curr_user.save()
            return render(request, "app_users/profile.html", context={"user": user, "user_list": user_list, "pk": pk})

        else:
            return render(request, "app_users/profile.html",context={"user": user,  "pk": pk})



class UpdateUserView(FormMixin, View):

    template_name = "app_users/update_user"

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        initial_data = {
            "first_name" : user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "city": user.profile.city,
            "tel": user.profile.tel
        }
        form = ProfileForm(initial=initial_data)
        return render(request, "app_users/update_user.html", context={"form": form, "pk": pk})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            curr_city = form.cleaned_data["city"]
            curr_tel = form.cleaned_data["tel"]
            print(curr_city, curr_tel)
            updated_user.profile.city = curr_city
            updated_user.profile.tel = curr_tel
            updated_user.save()
            return HttpResponseRedirect(f"/profile/{pk}/?")
        return render(request, self.template_name, context={"form": form, "user": user,  "pk": pk})


# Класс отвечающий за страницу создания Новости.
class NewsView(View):

    template_name = "app_users/newscreate.html"

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        form = NewsForm()
        return render(request, "app_users/newscreate.html", context={"form": form, "user": user, "pk": pk})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user.profile
            news.save()
            return HttpResponseRedirect("/")
        return render(request, "app_users/newscreate.html", context={"form": form, "user": user, "pk": pk})






