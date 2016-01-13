from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _ug
from easy_thumbnails.fields import ThumbnailerImageField
from MainAPP import hardcode


# Custom user which inherits from an AbstractUser and uses the code in
#  backends.py to authenticate and validate permissions
class Role(models.Model):
    name = models.CharField(
        max_length=hardcode.role_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.role_description_length,
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
            super(Role, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Role')
        verbose_name_plural = _ug('Roles')
        permissions = (
            ('query_role', 'Query Role'),
            ('list_role', 'List Roles'),
        )


class Privilege(models.Model):
    roles = models.ManyToManyField(
        Role,
        related_name='privileges',
        verbose_name=_ug('Roles')
    )
    created_by = models.ManyToManyField(
        'CustomUser',
        related_name='privileges_created',
        verbose_name=_ug('Created by')
    )
    action = models.CharField(
        max_length=hardcode.privilege_action_length,
        blank=False,
        null=False,
        verbose_name=_ug('Action')
    )
    can_read = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Can read?')
    )
    can_create = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Can create?')
    )
    can_update = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Can update?')
    )
    can_delete = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Can delete?')
    )
    can_execute = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_ug('Can execute?')
    )
    hidden = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        return "%s" % self.action

    def delete(self, *args):
        if self.hidden is True:
            super(Privilege, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Privilege')
        verbose_name_plural = _ug('Privileges')
        permissions = (
            ('query_privilege', 'Query Privilege'),
            ('list_privilege', 'List Privileges'),
        )


class Company(models.Model):
    name = models.CharField(
        max_length=hardcode.company_name_length,
        blank=False,
        null=False,
        verbose_name=_ug('Name')
    )
    description = models.CharField(
        max_length=hardcode.company_description_length,
        blank=False,
        null=False,
        verbose_name=_ug('Description')
    )
    phone = models.CharField(
        max_length=hardcode.company_phone_length,
        blank=False,
        null=False,
        verbose_name=_ug('Phone')
    )
    active = models.BooleanField(
        default=True,
        blank=True,
        verbose_name=_ug('Active')
    )

    def __str__(self):
        return "%s" % self.name

    def delete(self, *args):
        if self.hidden is True:
            super(Company, self).delete(*args)
        else:
            self.hidden = True
            self.save()

    class Meta:
        verbose_name = _ug('Company')
        verbose_name_plural = _ug('Companies')
        permissions = (
            ('query_company', 'Query Company'),
            ('list_company', 'List Companies'),
        )


class CustomUser(AbstractUser):
    middle_name = models.CharField(
        max_length=hardcode.user_middlename_length,
        blank=True,
        null=True,
        verbose_name=_ug('Middle Name')
    )
    mothers_name = models.CharField(
        max_length=hardcode.user_mothersname_length,
        blank=True,
        null=True,
        verbose_name=_ug('Mothers Name')
    )
    nickname = models.CharField(
        max_length=hardcode.user_nickname_length,
        blank=True,
        null=True,
        verbose_name=_ug('Nickname')
    )
    skype = models.CharField(
        max_length=hardcode.user_skype_length,
        blank=True,
        null=True,
        verbose_name=_ug('Skype')
    )
    company = models.ForeignKey(
        Company,
        related_name='employees',
        blank=True,
        null=True,
        verbose_name=_ug('Company')
    )
    supervisor = models.ForeignKey(
        'CustomUser',
        related_name='subordinates',
        blank=True,
        null=True,
        verbose_name=_ug('Supervisor')

    )
    avatar = ThumbnailerImageField(
        upload_to=hardcode.user_avatar_upload,
        default=hardcode.user_default_photo,
        blank=True,
        null=True,
        verbose_name=_ug('Profile picture')
    )
    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name=_ug('Birthday')
    )
    # gender = models.IntegerField(
    #     default=hardcode.GENDER_UNDEFINED,
    #     choices=hardcode.GENDER,
    #     blank=True,
    #     null=True,
    #     verbose_name=_ug('Gender')
    # )
    edition_date = models.DateTimeField(
        auto_now=True,
        verbose_name=_ug('Last edition date')
    )
    role = models.ManyToManyField(
        Role,
        related_name='customusers',
        verbose_name=_ug('Custom users')
    )

    class Meta:
        verbose_name = _ug('User')
        verbose_name_plural = _ug('Users')
        permissions = (
            ('query_customuser', 'Query User'),
            ('list_customuser', 'List Users'),
        )

    def save(self, *args, **kwargs):
        if self.pk is None:
            avatar = self.avatar
            self.avatar = None
            super(CustomUser, self).save(*args, **kwargs)
            self.avatar = avatar
        super(CustomUser, self).save(*args, **kwargs)

    def delete(self, *args):
        if self.active is False:
            super(CustomUser, self).delete(*args)
        else:
            self.active = False
            self.save()

    def __str__(self):
        return "%s - %s %s" % (self.username, self.first_name, self.last_name)

    def get_full_name(self):
        full_name = '%s %s %s %s' % (self.first_name, self.middle_name, self.last_name, self.mothers_name)
        return full_name.strip()

    def get_username(self):
        return "%s" % self.username

    def get_nickname(self):
        return "%s" % self.nickname

    def get_short_name(self):
        if self.nickname is None or self.nickname == '':
            return "%s" % self.username
        return self.get_nickname()

    def is_authorized(self):
        return self.is_active

    def is_admin(self):
        return self.is_staff

    def is_super(self):
        return self.is_superuser
