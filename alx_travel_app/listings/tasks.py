from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation(email, booking_ref):
    send_mail(
        subject="Payment Confirmation",
        message=f"payment for booking {booking_ref} was successful.",
        from_email="no-reply@alxtravel.com",
        recipient_list=[email],
        fail_silently=False,
    )
