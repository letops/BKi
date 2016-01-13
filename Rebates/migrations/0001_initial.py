# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Utilities', '0001_initial'),
        ('MainAPP', '0002_auto_20160112_2030'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approved', models.BooleanField(verbose_name='Approved?', default=False)),
                ('submitted', models.BooleanField(verbose_name='Submitted?', default=False)),
                ('rejected', models.BooleanField(verbose_name='Rejected?', default=False)),
                ('stalled', models.BooleanField(verbose_name='Stalled?', default=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Approval',
                'verbose_name_plural': 'Approvals',
                'permissions': (('query_approval', 'Query Approval'), ('list_approval', 'List Approvals')),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=45)),
                ('description', models.CharField(verbose_name='Description', max_length=256, blank=True, null=True)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('hidden', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(related_name='sons', to='Rebates.Post', null=True, verbose_name='Parent Post', blank=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'permissions': (('query_post', 'Query Post'), ('list_post', 'List Posts')),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('description', models.CharField(verbose_name='Description', max_length=1024, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(related_name='sons', to='Rebates.Project', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'permissions': (('query_project', 'Query Project'), ('list_project', 'List Projects')),
            },
        ),
        migrations.CreateModel(
            name='RawRebate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(verbose_name='Project Title', max_length=256)),
                ('minrebate', models.DecimalField(verbose_name='Minimum Rebate', null=True, max_digits=12, blank=True, decimal_places=2)),
                ('maxrebate', models.DecimalField(verbose_name='Maximum Rebate', null=True, max_digits=12, blank=True, decimal_places=2)),
                ('provider_type', models.SmallIntegerField(verbose_name='Provider Type', null=True, blank=True)),
                ('eligible_if_replacing', models.CharField(verbose_name='Eligible if replacing', max_length=255, blank=True, null=True)),
                ('eligible_if_installing', models.CharField(verbose_name='Eligible if installing', max_length=255, blank=True, null=True)),
                ('electric', models.BooleanField(verbose_name='Electric', default=False)),
                ('natural_gas', models.BooleanField(verbose_name='Natural gas', default=False)),
                ('water', models.BooleanField(verbose_name='Water', default=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('start_date', models.DateTimeField(verbose_name='Start date', null=True, blank=True)),
                ('end_date', models.DateTimeField(verbose_name='End date', null=True, blank=True)),
                ('active', models.BooleanField(verbose_name='Active', default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Raw Rebate',
                'verbose_name_plural': 'Raw Rebates',
                'permissions': (('query_rawrebate', 'Query Raw Rebate'), ('list_rawrebate', 'List Raw Rebates')),
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=45)),
                ('description', models.CharField(verbose_name='Description', max_length=45, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
                'permissions': (('query_unit', 'Query Unit'), ('list_unit', 'List Units')),
            },
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(verbose_name='URL', max_length=2048)),
                ('cached_until', models.DateTimeField(verbose_name='Cached until', null=True, blank=True)),
                ('valid', models.BooleanField(verbose_name='Valid', default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('utility', models.ForeignKey(related_name='url', to='Utilities.Utility', verbose_name='Utility')),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
                'permissions': (('query_url', 'Query URL'), ('list_url', 'List URLs')),
            },
        ),
        migrations.CreateModel(
            name='URLMonitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shouldbe', models.TextField(verbose_name='Should Be', null=True, blank=True)),
                ('result', models.SmallIntegerField(verbose_name='Result', null=True, blank=True)),
                ('last_checked', models.DateTimeField(verbose_name='Last checked', null=True, blank=True)),
                ('verified', models.DateTimeField(verbose_name='Verified', null=True, blank=True)),
                ('check_every_mins', models.IntegerField(verbose_name='Check every', null=True, blank=True)),
                ('check_on_date', models.DateTimeField(verbose_name='Checked on', null=True, blank=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('hidden', models.BooleanField(default=False)),
                ('role', models.ForeignKey(related_name='urlmonitor', to='MainAPP.Role', verbose_name='Role')),
                ('url', models.ForeignKey(related_name='urlmonitor', to='Rebates.URL', verbose_name='URL')),
                ('user', models.ForeignKey(related_name='urlmonitor', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('user_verified', models.ForeignKey(related_name='urlmonitor_verified', to=settings.AUTH_USER_MODEL, verbose_name='User Verified')),
            ],
            options={
                'verbose_name': 'URL Monitor',
                'verbose_name_plural': 'URL Monitors',
                'permissions': (('query_urlmonitor', 'Query URL Monitor'), ('list_urlmonitor', 'List URL Monitors')),
            },
        ),
        migrations.AddField(
            model_name='rawrebate',
            name='more_info_link',
            field=models.ForeignKey(related_name='rawrebates_moreinfo', to='Rebates.URL', null=True, verbose_name='More info link', blank=True),
        ),
        migrations.AddField(
            model_name='rawrebate',
            name='published_rebate',
            field=models.ForeignKey(related_name='posts_published', to='Rebates.RawRebate', verbose_name='Published Rebate'),
        ),
        migrations.AddField(
            model_name='rawrebate',
            name='source_link',
            field=models.ForeignKey(related_name='rawrebates_source', to='Rebates.URL', null=True, verbose_name='Source link', blank=True),
        ),
        migrations.AddField(
            model_name='rawrebate',
            name='unit',
            field=models.ForeignKey(verbose_name='Unit', to='Rebates.Unit'),
        ),
        migrations.AddField(
            model_name='rawrebate',
            name='utility',
            field=models.ForeignKey(related_name='rawrebate', to='Utilities.Utility', verbose_name='Utility'),
        ),
        migrations.AddField(
            model_name='post',
            name='rawrebate',
            field=models.ForeignKey(related_name='posts', to='Rebates.RawRebate', verbose_name='Raw Rebate'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL, null=True, verbose_name='User', blank=True),
        ),
        migrations.AddField(
            model_name='approval',
            name='post',
            field=models.ForeignKey(related_name='approvals', to='Rebates.Post', verbose_name='Post'),
        ),
        migrations.AddField(
            model_name='approval',
            name='rawrebate',
            field=models.ForeignKey(related_name='approvals', to='Rebates.RawRebate', verbose_name='Raw Rebate'),
        ),
        migrations.AddField(
            model_name='approval',
            name='user',
            field=models.ForeignKey(related_name='approvals', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
