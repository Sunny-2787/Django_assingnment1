from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save,sender = User)
def send_activation_email(sender,instance ,created, **kwargs):
    if created:
        Token = default_token_generator.make_token(instance)
        activate_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{Token}/"
        subject = "Activate Your Account"
        message = f"Hi , {instance.username} \n Please activate your account bia link !\n {activate_url}\n\nThank you."
        recever = [instance.email]
        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER ,recever)
        except Exception as e:
            print(f"Faiild to sent mail to {instance.email} : {str(e )}")


@receiver(post_save,sender = User)
def assignrole(sender,instance,created,**kwargs):
    if created:
        user_g,created = Group.objects.get_or_create(name='participant')
        instance.groups.add(user_g)
        instance.save

    