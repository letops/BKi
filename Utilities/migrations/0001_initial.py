# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('shortname', models.CharField(verbose_name='Short name', max_length=10, blank=True, null=True)),
                ('code', models.CharField(verbose_name='Code', max_length=6, blank=True, null=True)),
                ('web', models.CharField(verbose_name='Web', max_length=1024, blank=True, null=True)),
                ('phone', models.CharField(verbose_name='Phone', max_length=45, blank=True, null=True)),
                ('default_lawn_size', models.CharField(verbose_name='Default Lawn Size', max_length=255, blank=True, null=True)),
                ('through_1979', models.CharField(verbose_name='Through 1979', max_length=255, blank=True, null=True)),
                ('between_1980_1989', models.CharField(verbose_name='Between 1980-1989', max_length=255, blank=True, null=True)),
                ('between_1990_2002', models.CharField(verbose_name='Between 1990-2002', max_length=255, blank=True, null=True)),
                ('country', models.CharField(verbose_name='Country', max_length=6, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(related_name='sons', to='Utilities.PoliticalArea', null=True, verbose_name='Parent', blank=True)),
            ],
            options={
                'verbose_name': 'Political Area',
                'verbose_name_plural': 'Political Areas',
                'permissions': (('query_politicalarea', 'Query Political Area'), ('list_politicalarea', 'List Political Area')),
            },
        ),
        migrations.CreateModel(
            name='PoliticalAreaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=45)),
                ('hidden', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(related_name='political_area_type', to='Utilities.PoliticalAreaType', null=True, verbose_name='Political Area Type', blank=True)),
            ],
            options={
                'verbose_name': 'Political Area Type',
                'verbose_name_plural': 'Political Area Types',
                'permissions': (('query_politicalareatype', 'Query Political Area Type'), ('list_politicalareatype', 'List Political Area Types')),
            },
        ),
        migrations.CreateModel(
            name='PoliticalAreaUtility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('political_area', models.ForeignKey(related_name='political_area_utilities', to='Utilities.PoliticalArea', verbose_name='Political Area')),
            ],
            options={
                'verbose_name': 'Political Area Utility',
                'verbose_name_plural': 'Political Area Utilities',
                'permissions': (('query_politicalareautility', 'Query Political Area Utility'), ('list_politicalareautility', 'List Political Area Utilities')),
            },
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=1024)),
                ('shortname', models.CharField(verbose_name='Short Name', max_length=45, blank=True, null=True)),
                ('web', models.CharField(verbose_name='Web', max_length=1024, blank=True, null=True)),
                ('phone', models.CharField(verbose_name='Phone', max_length=45, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Utility',
                'verbose_name_plural': 'Utilities',
                'permissions': (('query_utility', 'Query Utility'), ('list_utility', 'List Utilities')),
            },
        ),
        migrations.CreateModel(
            name='UtilityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=45)),
                ('description', models.CharField(verbose_name='Description', max_length=255, blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Utility Type',
                'verbose_name_plural': 'Utility Types',
                'permissions': (('query_utilitytype', 'Query Utility Type'), ('list_utilitytype', 'List Utility Types')),
            },
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=10)),
                ('hidden', models.BooleanField(default=False)),
                ('political_area', models.ForeignKey(related_name='zips', to='Utilities.PoliticalArea', verbose_name='Political Area')),
            ],
            options={
                'verbose_name': 'Zip',
                'verbose_name_plural': 'Zips',
                'permissions': (('query_zip', 'Query Zip'), ('list_zip', 'List Zip')),
            },
        ),
        migrations.AddField(
            model_name='utility',
            name='utility_type',
            field=models.ForeignKey(related_name='utilities', to='Utilities.UtilityType', verbose_name='Utility Type'),
        ),
        migrations.AddField(
            model_name='politicalareautility',
            name='utility',
            field=models.ForeignKey(related_name='political_area_utilities', to='Utilities.Utility', verbose_name='Utility'),
        ),
        migrations.AddField(
            model_name='politicalarea',
            name='political_area_type',
            field=models.ForeignKey(related_name='political_area', to='Utilities.PoliticalAreaType', verbose_name='Political Area Type'),
        ),
    ]
