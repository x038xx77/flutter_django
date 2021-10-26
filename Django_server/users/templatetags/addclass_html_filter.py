from django import template
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from web_med_plist.settings import AUTH_USER_MODEL


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def convert_minute_format(sec):
    convert_min = 60*sec
    sec = convert_min % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if convert_min >= 3600:
        return "%02dч. %02dмин." % (hour, min)
    else:
        return "%02dмин." % (min)




# @register.filter
# def user_client_first_name(user_appointment):
#     user_appointment_meeting = get_object_or_404(
#         User, username=user_appointment)
#     person = {
#         'first_name': user_appointment_meeting.first_name,
#         }
#     return "{p[first_name]}".format(p=person)


# @register.filter
# def user_client_last_name(user_appointment):
#     user_appointment_meeting = get_object_or_404(
#         User, username=user_appointment)
#     person = {
#         'last_name': user_appointment_meeting.last_name,
#         }
#     return "{p[last_name]}".format(p=person)


# @register.filter
# def user_client_username(user_appointment):
#     user_appointment_meeting = get_object_or_404(
#         User, username=user_appointment)
#     person = {
#         'user_name': user_appointment_meeting.username,
#         }
#     return "{p[user_name]}".format(p=person)


# @register.filter
# def user_client_email(user_appointment):
#     user_appointment_meeting = get_object_or_404(
#         User, username=user_appointment)
#     person = {
#         'email': user_appointment_meeting.email,
#         }
#     return "{p[email]}".format(p=person)


# @register.filter
# def user_client_birthday(user_appointment):
#     profile_appointment_meeting = User.objects.filter(birthday=user_appointment)
#     person = {
#         'birthday': profile_appointment_meeting.birthday,
#         }
#     return "{p[birthday]}".format(p=person)


# @register.filter
# def user_client_phone(user_appointment):
#     profile_appointment_meeting = User.objects.filter(phone=user_appointment)
#     person = {
#         'phone': User.phone
#         }
#     return "{p[phone]}".format(p=person)
