from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    """Additional profile data not held within the standard User model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        default="profiles/default.jpg",
        upload_to="profiles",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        default_image = self._meta.get_field("image").default

        if not self.image or self.image.name == default_image:
            return

        try:
            self.image.open("rb")
            thumbnail_image = Image.open(self.image)
        except (FileNotFoundError, ValueError):
            return

        max_size = (300, 300)

        if thumbnail_image.width <= 300 and thumbnail_image.height <= 300:
            return

        image_types = {
            "jpg": "JPEG",
            "jpeg": "JPEG",
            "png": "PNG",
            "gif": "GIF",
            "tif": "TIFF",
            "tiff": "TIFF",
        }

        thumbnail_image.thumbnail(max_size, Image.Resampling.LANCZOS)

        image_format = thumbnail_image.format
        if not image_format:
            filename_suffix = self.image.name.rsplit(".", 1)[-1].lower()
            image_format = image_types.get(filename_suffix, "JPEG")

        if image_format.upper() == "JPEG" and thumbnail_image.mode in ("RGBA", "P"):
            thumbnail_image = thumbnail_image.convert("RGB")

        buffer = BytesIO()
        thumbnail_image.save(buffer, format=image_format)

        # Important:
        # Use self.image.name, not self.image.file.name.
        # self.image.name is storage-relative, e.g. profiles/image.png.
        # self.image.file.name may be an absolute filesystem path, which Django rejects.
        self.image.save(
            self.image.name,
            ContentFile(buffer.getvalue()),
            save=False,
        )

        super().save(update_fields=["image"])


def create_profile(sender, created, instance, **kwargs):
    """Store the user profile in the database."""

    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)