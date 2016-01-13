from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import ugettext as _ug
from MainAPP import models as main_models
from Rebates import hardcode
from Utilities import models as utility_models


class Unit(models.Model):
    name = models.CharField(
        max_length=hardcode.unit_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.unit_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Unit, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Unit')
        verbose_name_plural = _ug('Units')
        permissions = (
            ('query_unit', 'Query Unit'),
            ('list_unit', 'List Units'),
        )


class Project(models.Model):
    name = models.CharField(
        max_length=hardcode.project_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.project_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description')
    )
    parent = models.ForeignKey(
        'Project',
        related_name='sons',
        blank=False,
        null=False,
        verbose_name=_ug('Parent')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Project, self).delete(*args)
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


class URL(models.Model):
    url = models.CharField(
        max_length=hardcode.url_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('URL')
    )
    cached_until = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Cached until')
    )
    utility = models.ForeignKey(
        utility_models.Utility,
        related_name='url',
        blank=False,
        null=False,
        verbose_name=_ug('Utility')
    )
    valid = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Valid')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.url

    def delete(self, *args):
        if self.hidden is True:
            super(URL, self).delete(*args)
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


class RawRebate(models.Model):
    project_title = models.CharField(
        max_length=hardcode.rawrebate_projecttitle_length,
        blank=False,
        null=False,
        verbose_name=_ug('Project Title')
    )
    utility = models.ForeignKey(
        utility_models.Utility,
        related_name='rawrebate',
        blank=False,
        null=False,
        verbose_name=_ug('Utility')
    )
    minrebate = models.DecimalField(
        max_digits=hardcode.rawrebate_minrebate_maxdigits,
        decimal_places=hardcode.rawrebate_minrebate_decimalplaces,
        blank=True,
        null=True,
        verbose_name=_ug('Minimum Rebate')
    )
    maxrebate = models.DecimalField(
        max_digits=hardcode.rawrebate_maxrebate_maxdigits,
        decimal_places=hardcode.rawrebate_maxrebate_decimalplaces,
        blank=True,
        null=True,
        verbose_name=_ug('Maximum Rebate')
    )
    unit = models.ForeignKey(
        Unit,
        blank=False,
        null=False,
        verbose_name=_ug('Unit')
    )
    provider_type = models.SmallIntegerField(
        blank=True,
        null=True,
        verbose_name=_ug('Provider Type')
    )
    eligible_if_replacing = models.CharField(
        max_length=hardcode.rawrebate_eligibleifreplacing_length,
        blank=True,
        null=True,
        verbose_name=_ug('Eligible if replacing')
    )
    eligible_if_installing = models.CharField(
        max_length=hardcode.rawrebate_eligibleifinstalling_length,
        blank=True,
        null=True,
        verbose_name=_ug('Eligible if installing')
    )
    electric = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Electric')
    )
    natural_gas = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Natural gas')
    )
    water = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Water')
    )
    source_link = models.ForeignKey(
        URL,
        related_name='rawrebates_source',
        blank=True,
        null=True,
        verbose_name=_ug('Source link')
    )
    more_info_link = models.ForeignKey(
        URL,
        related_name='rawrebates_moreinfo',
        blank=True,
        null=True,
        verbose_name=_ug('More info link')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_ug('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_ug('Updated at')
    )
    start_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Start date')
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('End date')
    )
    active = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Active')
    )
    published_rebate = models.ForeignKey(
        'RawRebate',
        related_name='posts_published',
        blank=False,
        null=False,
        verbose_name=_ug('Published Rebate')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.project_title

    def delete(self, *args):
        if self.hidden is True:
            super(RawRebate, self).delete(*args)
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


class URLMonitor(models.Model):
    shouldbe = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ug('Should Be')
    )
    url = models.ForeignKey(
        URL,
        related_name='urlmonitor',
        blank=False,
        null=False,
        verbose_name=_ug('URL')
    )
    result = models.SmallIntegerField(
        blank=True,
        null=True,
        verbose_name=_ug('Result')
    )
    last_checked = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Last checked')
    )
    user = models.ForeignKey(
        main_models.CustomUser,
        related_name='urlmonitor',
        blank=False,
        null=False,
        verbose_name=_ug('User')
    )
    role = models.ForeignKey(
        main_models.Role,
        related_name='urlmonitor',
        blank=False,
        null=False,
        verbose_name=_ug('Role')
    )
    verified = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Verified')
    )
    user_verified = models.ForeignKey(
        main_models.CustomUser,
        related_name='urlmonitor_verified',
        blank=False,
        null=False,
        verbose_name=_ug('User Verified')
    )
    check_every_mins = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_ug('Check every')
    )
    check_on_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_ug('Checked on')
    )
    active = models.BooleanField(
        default=True,
        blank=True,
        verbose_name=_ug('Active')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s - %s" % (self.user, self.shouldbe)

    def delete(self, *args):
        if self.hidden is True:
            super(URLMonitor, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('URL Monitor')
        verbose_name_plural = _ug('URL Monitors')
        permissions = (
            ('query_urlmonitor', 'Query URL Monitor'),
            ('list_urlmonitor', 'List URL Monitors'),
        )


class Post(models.Model):
    name = models.CharField(
        max_length=hardcode.post_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.post_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description')
    )
    rawrebate = models.ForeignKey(
        RawRebate,
        related_name='posts',
        blank=False,
        null=False,
        verbose_name=_ug('Raw Rebate')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_ug('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_ug('Updated at')
    )
    parent = models.ForeignKey(
        'Post',
        related_name='sons',
        blank=True,
        null=True,
        verbose_name=_ug('Parent Post')
    )
    user = models.ForeignKey(
        main_models.CustomUser,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name=_ug('User')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Post, self).delete(*args)
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


class Approval(models.Model):
    rawrebate = models.ForeignKey(
        RawRebate,
        related_name='approvals',
        blank=False,
        null=False,
        verbose_name=_ug('Raw Rebate')
    )
    user = models.ForeignKey(
        main_models.CustomUser,
        related_name='approvals',
        blank=False,
        null=False,
        verbose_name=_ug('User')
    )
    approved = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Approved?')
    )
    submitted = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Submitted?')
    )
    rejected = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Rejected?')
    )
    stalled = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Stalled?')
    )
    post = models.ForeignKey(
        Post,
        related_name='approvals',
        blank=False,
        null=False,
        verbose_name=_ug('Post')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_ug('Created at')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s - %s" % (self.name, self.rawrebate)

    def delete(self, *args):
        if self.hidden is True:
            super(Approval, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Approval')
        verbose_name_plural = _ug('Approvals')
        permissions = (
            ('query_approval', 'Query Approval'),
            ('list_approval', 'List Approvals'),
        )
