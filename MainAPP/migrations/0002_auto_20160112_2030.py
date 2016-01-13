# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('MainAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=124)),
                ('description', models.CharField(verbose_name='Description', max_length=255)),
                ('phone', models.CharField(verbose_name='Phone', max_length=45)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'permissions': (('query_company', 'Query Company'), ('list_company', 'List Companies')),
            },
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(verbose_name='Action', max_length=45)),
                ('can_read', models.BooleanField(verbose_name='Can read?', default=False)),
                ('can_create', models.BooleanField(verbose_name='Can create?', default=False)),
                ('can_update', models.BooleanField(verbose_name='Can update?', default=False)),
                ('can_delete', models.BooleanField(verbose_name='Can delete?', default=False)),
                ('can_execute', models.BooleanField(verbose_name='Can execute?', default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Privilege',
                'verbose_name_plural': 'Privileges',
                'permissions': (('query_privilege', 'Query Privilege'), ('list_privilege', 'List Privileges')),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=45)),
                ('description', models.CharField(verbose_name='Description', max_length=256, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'permissions': (('query_role', 'Query Role'), ('list_role', 'List Roles')),
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='hidden',
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(verbose_name='Middle Name', max_length=45, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mothers_name',
            field=models.CharField(verbose_name='Mothers Name', max_length=45, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skype',
            field=models.CharField(verbose_name='Skype', max_length=45, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='supervisor',
            field=models.ForeignKey(related_name='subordinates', to=settings.AUTH_USER_MODEL, null=True, verbose_name='Supervisor', blank=True),
        ),
        migrations.AddField(
            model_name='privilege',
            name='created_by',
            field=models.ManyToManyField(verbose_name='Created by', related_name='privileges_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privilege',
            name='roles',
            field=models.ManyToManyField(verbose_name='Roles', related_name='privileges', to='MainAPP.Role'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(related_name='employees', to='MainAPP.Company', null=True, verbose_name='Company', blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ManyToManyField(verbose_name='Custom users', related_name='customusers', to='MainAPP.Role'),
        ),
    ]
