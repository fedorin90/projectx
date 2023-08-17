from django.core.mail import send_mail, send_mass_mail


def send_contact_info(first_name, last_name, email, message):
    subject = "Website contact"
    body = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'message': message,
    }
    message = "\n".join(body.values())
    send_mail(subject, message, 'fedorin.mir@gamil.com', ['fedorin.mir@gmail.com'])
