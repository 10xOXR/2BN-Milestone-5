from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

class Profile(models.Model):
    """ Additional profile data not held within the standard User model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='prof_img/default.jpg',
        upload_to="prof_img",
        blank=True,
        null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            thumb = (300, 300)
            img.thumbnail(thumb)
            img.save(self.image.path)


def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
