# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
import django.contrib.auth.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('nikename', models.CharField(max_length=30, verbose_name='昵称', default='')),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', to='auth.Group', blank=True, verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_query_name='user', to='auth.Permission', blank=True, verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=50, verbose_name='验证码', default='')),
                ('eamil', models.CharField(max_length=30, verbose_name='邮箱')),
                ('send_type', models.CharField(max_length=30, verbose_name='验证码类型', choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')])),
                ('send_time', models.DateTimeField(verbose_name='发送时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '邮箱验证码',
                'verbose_name': '邮箱验证码',
            },
        ),
    ]
