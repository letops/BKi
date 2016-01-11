from django.db import models
from django.utils.translation import ugettext as _ug
from easy_thumbnails.fields import ThumbnailerImageField


class Project(models.Model):
    name = models.CharField(
        max_length=config.project_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name'))
    description = models.CharField(
        max_length=config.project_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description'))
    parent = models.ForeignKey(
        Project,
        related_name='sons',
        blank=False,
        null=False,
        verbose_name=_ug('Parent'))
    hidden = models.BooleanField(
        default=False,
        blank=True)

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Event, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Project')
        verbose_name_plural = _ug('Projects')
        permissions = (
            ('query_project', 'Query Project'),
            ('list_project', 'List Projects'),
        )


class RawRebate(models.Model):
    project_title = models.CharField(
        max_length=config.rawrebate_projecttitle_length,
        blank=False,
        null=False,
        verbose_name=_ug('Project Title'))
    minrebate = models.CharField(
        max_length=config.rawrebate_minrebate_length,
        blank=True,
        null=True,
        verbose_name=_ug('Minimum Rebate'))
    maxrebate = models.CharField(
        max_length=config.rawrebate_maxrebate_length,
        blank=True,
        null=True,
        verbose_name=_ug('Maximum Rebate'))
    providertype = models.ForeignKey(
        Provider
        blank=True,
        null=True,
        verbose_name=_ug('Provider Type'))

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Event, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Raw Rebate')
        verbose_name_plural = _ug('Raw Rebates')
        permissions = (
            ('query_rawrebate', 'Query Raw Rebate'),
            ('list_rawrebate', 'List Raw Rebates'),
        )


class URL(models.Model):
    url = models.CharField(
        max_length=config.url_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('URL'))
    cached_until = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Cached until'))
    utility = models.ForeignKey(
        related_name='url',
        blank=False,
        null=False,
        verbose_name=_ug('Utility'))
    valid = models.BooleanField(
        blank=True
        null=True
        verbose_name=_ug('Valid'))
    hidden = models.BooleanField(
        default=False,
        blank=True)

    def __str__(self):
        return "%s" % self.url

    def delete(self, *args):
        if self.hidden is True:
            super(Event, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('URL')
        verbose_name_plural = _ug('URLs')
        permissions = (
            ('query_url', 'Query URL'),
            ('list_url', 'List URLs'),
        )


class Post(models.Model):
    name = models.CharField(
        max_length=config.post_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name'))
    description = models.CharField(
        max_length=config.post_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description'))

    hidden = models.BooleanField(
        default=False,
        blank=True)

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Event, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Post')
        verbose_name_plural = _ug('Posts')
        permissions = (
            ('query_post', 'Query Post'),
            ('list_post', 'List Posts'),
        )
