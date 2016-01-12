from django.db import models
from django.utils.translation import ugettext as _ug
from Utilities import hardcode


class UtilityType(models.Model):
    name = models.CharField(
        max_length=hardcode.utilitytype_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.utilitytype_description_length,
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
            super(UtilityType, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Utility Type')
        verbose_name_plural = _ug('Utility Types')
        permissions = (
            ('query_utilitytype', 'Query Utility Type'),
            ('list_utilitytype', 'List Utility Types'),
        )


class Utility(models.Model):
    name = models.CharField(
        max_length=hardcode.utility_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    shortname = models.CharField(
        max_length=hardcode.utility_shortname_length,
        blank=True,
        null=True,
        verbose_name=_ug('Short Name')
    )
    web = models.CharField(
        max_length=hardcode.utility_web_length,
        blank=True,
        null=True,
        verbose_name=_ug('Web')
    )
    phone = models.CharField(
        max_length=hardcode.utility_phone_length,
        blank=True,
        null=True,
        verbose_name=_ug('Phone')
    )
    utility_type = models.ForeignKey(
        UtilityType,
        related_name='utilities',
        blank=False,
        null=False,
        verbose_name=_ug('Utility Type')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Utility, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Utility')
        verbose_name_plural = _ug('Utilities')
        permissions = (
            ('query_utility', 'Query Utility'),
            ('list_utility', 'List Utilities'),
        )


class PoliticalAreaUtility(models.Model):
    utility = models.ForeignKey(
        Utility,
        related_name='political_area_utilities',
        blank=False,
        null=False,
        verbose_name=_ug('Utility')
    )
    political_area = models.ForeignKey(
        PoliticalArea,
        related_name='political_area_utilities',
        blank=False,
        null=False,
        verbose_name=_ug('Political Area')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s %s" % (self.utility, self.political_area)

    def delete(self, *args):
        if self.hidden is True:
            super(PoliticalAreaUtility, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Political Area Utility')
        verbose_name_plural = _ug('Political Area Utilities')
        permissions = (
            ('query_politicalareautility', 'Query Political Area Utility'),
            ('list_politicalareautility', 'List Political Area Utilities'),
        )


class PoliticalAreaType(models.Model):
    name = models.CharField(
        max_length=hardcode.politicalareatype_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    parent = models.ForeignKey(
        'PoliticalAreaType',
        related_name='political_area_type',
        blank=True,
        null=True,
        verbose_name=_ug('Political Area Type')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(PoliticalAreaType, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Political Area Type')
        verbose_name_plural = _ug('Political Area Types')
        permissions = (
            ('query_politicalareatype', 'Query Political Area Type'),
            ('list_politicalareatype', 'List Political Area Types'),
        )


class PoliticalArea(models.Model):
    name = models.CharField(
        max_length=hardcode.politicalarea_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    shortname = models.CharField(
        max_length=hardcode.politicalarea_shortname_length,
        blank=True,
        null=True,
        verbose_name=_ug('Short name')
    )
    political_area_type = models.ForeignKey(
        PoliticalAreaType,
        related_name='political_area',
        blank=False,
        null=False,
        verbose_name=_ug('Political Area Type')
    )
    parent = models.ForeignKey(
        'PoliticalArea',
        related_name='sons',
        blank=True,
        null=True,
        verbose_name=_ug('Parent')
    )
    code = models.CharField(
        max_length=hardcode.politicalarea_code_length,
        blank=True,
        null=True,
        verbose_name=_ug('Code')
    )
    web = models.CharField(
        max_length=hardcode.politicalarea_web_length,
        blank=True,
        null=True,
        verbose_name=_ug('Web')
    )
    phone = models.CharField(
        max_length=hardcode.politicalarea_phone_length,
        blank=True,
        null=True,
        verbose_name=_ug('Phone')
    )
    default_lawn_size = models.CharField(
        max_length=hardcode.politicalarea_defaultlawnsize_length,
        blank=True,
        null=True,
        verbose_name=_ug('Default Lawn Size')
    )
    through_1979 = models.CharField(
        max_length=hardcode.politicalarea_through1979_length,
        blank=True,
        null=True,
        verbose_name=_ug('Through 1979')
    )
    between_1980_1989 = models.CharField(
        max_length=hardcode.politicalarea_between19801989_length,
        blank=True,
        null=True,
        verbose_name=_ug('Between 1980-1989')
    )
    between_1990_2002 = models.CharField(
        max_length=hardcode.politicalarea_between19902002_length,
        blank=True,
        null=True,
        verbose_name=_ug('Between 1990-2002')
    )
    country = models.CharField(
        max_length=hardcode.politicalarea_country_length,
        blank=True,
        null=True,
        verbose_name=_ug('Country')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(PoliticalArea, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Political Area')
        verbose_name_plural = _ug('Political Areas')
        permissions = (
            ('query_politicalarea', 'Query Political Area'),
            ('list_politicalarea', 'List Political Area'),
        )


class Zip(models.Model):
    name = models.CharField(
        max_length=hardcode.zip_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    political_area = models.ForeignKey(
        PoliticalArea,
        related_name='zips',
        blank=False,
        null=False,
        verbose_name=_ug('Political Area')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Zip, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Zip')
        verbose_name_plural = _ug('Zips')
        permissions = (
            ('query_zip', 'Query Zip'),
            ('list_zip', 'List Zip'),
        )
