from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed,post_delete,post_save
from django.dispatch import receiver
from Tasks.models import Event,RSVP
from django.conf import settings


@receiver(post_save,sender =RSVP)
def sendmail_to_user(sender,instance,created,**kwargs):
    if created:

        user = instance.user
        event = instance.event

        subject = f"RSVP Confirmation: {event.name}"
        message = (
            f"Hi {user.username},\n\n"
            f"You have successfully RSVP'd for '{event.name}'.\n"
            f"Status: {instance.get_status_display()}.\n"
            f"Event Date: {event.date}\n"
            f"Location: {event.location}\n\n"
            f"Thank you for your response!"
        )
        from_email = "EMAIL_HOST_USER"
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)
