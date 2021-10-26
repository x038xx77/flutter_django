from django.core.mail import send_mail
# Функция отправки сообщения
def email_form(subject, content, sender_email, addressee_email):
    send_mail(
        subject, content,
        sender_email,
        [addressee_email])
