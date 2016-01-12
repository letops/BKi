from django.utils.translation import ugettext as _ug
import os

role_name_length = 45
role_description_length = 256

user_nickname_length = 30
user_default_photo = "users/avatars/no-img.jpg"
user_description_length = 500
GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_UNDEFINED = 2
GENDER = (
    (GENDER_MALE, _ug('Male')),
    (GENDER_FEMALE, _ug('Female')),
    (GENDER_UNDEFINED, _ug('Prefer not to say')),
)

def user_avatar_upload(instance, filename):
    fn, ext = os.path.splitext(filename)
    return "users/avatars/{id}{ext}".format(id=instance.pk, ext=ext)