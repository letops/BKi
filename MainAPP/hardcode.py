from django.utils.translation import ugettext as _ug
import os

role_name_length = 45
role_description_length = 256

privilege_action_length = 45

company_name_length = 124
company_description_length = 255
company_phone_length = 45


user_nickname_length = 30
user_middlename_length = 45
user_mothersname_length = 45
user_skype_length = 45
user_default_photo = "users/avatars/no-img.jpg"

def user_avatar_upload(instance, filename):
    fn, ext = os.path.splitext(filename)
    return "users/avatars/{id}{ext}".format(id=instance.pk, ext=ext)