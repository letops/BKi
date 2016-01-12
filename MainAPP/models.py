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
    action = models.CharField(
        max_length=hardcode.privilege_action_length,
        blank=False,
        null=False,
        verbose_name=_ug('Action')
    )
    read
    create
    update
    delete
    execute
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


class CustomUser(AbstractUser):
    nickname = models.CharField(
        max_length=hardcode.user_nickname_length,
        blank=True,
        null=True,
        verbose_name=_ug('Nickname')
    )
    role = models.ManyToManyField(
        Role,
        related_name='customusers',
        verbose_name=_ug('Custom users')
    )
    privileges = models.ManyToManyField(
        Privilege,
        related_name='customusers',
        verbose_name=_ug('Privileges')
    )
    **
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
    description = models.CharField(
        max_length=hardcode.user_description_length,
        blank=True,
        null=True,
        verbose_name=_ug('Description')
    )
    gender = models.IntegerField(
        default=hardcode.GENDER_UNDEFINED,
        choices=hardcode.GENDER,
        blank=True,
        null=True,
        verbose_name=_ug('Gender')
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_ug('Creation date')
    )
    edition_date = models.DateTimeField(
        auto_now=True,
        verbose_name=_ug('Last edition date')
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
        return super(CustomUser, self).get_full_name()

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
