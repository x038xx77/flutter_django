from django.core.mail import send_mail


def email_user(user, token_generator):
    send_mail(
        'Subject. Confirmation code',
        f'Confirmation code: {token_generator.make_token(user)}',
        'registration@yambd.com',
        (user.email,),
        fail_silently=False,
    )


def is_auth_path(request):
    return request.path.split('/')[-3] == 'auth'
