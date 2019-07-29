from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files import File
from django.core.files.storage import default_storage as storage
from pathlib import Path
import os
import mimetypes


class Profile(models.Model):
    """ Additional profile data not held within the standard User model """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    image = models.ImageField(
        default="profiles/default.jpg",
        upload_to="profiles",
        blank=True,
        null=True
    )
    user_bugs = models.IntegerField(
        default=0
    )
    user_comments = models.IntegerField(
        default=0
    )
    user_features = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        thumbnail_image = Image.open(self.image)
        i_width, i_height = thumbnail_image.size
        max_size = (300, 300)

        image_types = {
            'jpg': 'JPEG',
            'jpeg': 'JPEG',
            'png': 'PNG',
            'gif': 'GIF',
            'tif': 'TIFF',
        }

        if i_width > 300:
            buffer = BytesIO()
            thumbnail_image.thumbnail(max_size, Image.ANTIALIAS)
            filename_suffix = thumbnail_image.format.lower()
            image_format = image_types[filename_suffix]
            thumbnail_image.save(buffer, format=image_format)
            file_object = File(buffer)
            self.image.save(self.image.file.name, file_object)


def create_profile(sender, created, instance, **kwargs):
    """ Store the user profile in the database """

    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)


class BadgeType(models.Model):
    """ Defines the types of Badges users can achieve """

    badge_type = models.CharField(
        max_length=25,
        null=True
    )

    class Meta:
        verbose_name = ("Badge Type")
        verbose_name_plural = ("Badge Types")

    def __str__(self):
        return self.badge_type


class Badges(models.Model):
    """ Records which users have achieved which badges """

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    badge_type = models.ForeignKey(
        BadgeType,
        null=True
    )

    class Meta:
        verbose_name = ("Badge")
        verbose_name_plural = ("Badges")

    def __str__(self):
        return "User {0} assigned Badge {1}".format(
            self.user_id, self.badge_type
            )
