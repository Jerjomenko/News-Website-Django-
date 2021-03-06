# Generated by Django 3.2.9 on 2022-02-02 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='Ник')),
                ('text', models.TextField(default='', max_length=700, verbose_name='коментарий')),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coments', to='app_users.news', verbose_name='Новости')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Коментарии',
                'verbose_name_plural': 'Коментарии',
                'db_table': 'coments',
            },
        ),
    ]
