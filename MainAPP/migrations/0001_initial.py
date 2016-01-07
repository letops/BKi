# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models
import MainAPP.hardcode


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('nickname', models.CharField(verbose_name='Nickname', null=True, blank=True, max_length=30)),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Profile picture', null=True, blank=True, upload_to=MainAPP.hardcode.user_avatar_upload, default='users/avatars/no-img.jpg')),
                ('birthday', models.DateField(verbose_name='Birthday', null=True, blank=True)),
                ('description', models.CharField(verbose_name='Description', null=True, blank=True, max_length=500)),
                ('gender', models.IntegerField(verbose_name='Gender', null=True, blank=True, default=2, choices=[(0, 'Male'), (1, 'Female'), (2, 'Prefer not to say')])),
                ('creation_date', models.DateTimeField(verbose_name='Creation date', auto_now_add=True)),
                ('edition_date', models.DateTimeField(verbose_name='Last edition date', auto_now=True)),
                ('hidden', models.BooleanField(verbose_name='Hidden', default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', blank=True, to='auth.Group', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', blank=True, to='auth.Permission', related_name='user_set', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'User',
                'permissions': (('query_customuser', 'Query User'), ('list_customuser', 'List Users')),
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
