from __future__ import unicode_literals

from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.forms import ModelForm
from resizeimage import resizeimage


class OfficerRole(models.Model):
    title = models.CharField(max_length=300)
    list_position = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class Officer(models.Model):
    name_first = models.CharField('First Name', max_length=300)
    name_last = models.CharField('Last Name', max_length=300)
    role = models.ForeignKey(OfficerRole, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='officer_photos')
    bio = models.TextField()

    def __str__(self):
        return '{} {} - {}'.format(self.name_first, self.name_last, self.role)


class Membership(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class MessageType(models.Model):
    title = models.CharField(max_length=300)
    list_position = models.IntegerField()
    responsible_officer_role = models.ForeignKey(OfficerRole, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()
    message_type = models.ForeignKey(MessageType, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_type', 'name', 'email', 'message']


class JobPosting(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    company_name = models.CharField(max_length=300)
    company_blurb = models.TextField()
    company_url = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    expiration_date = models.DateField()
    contact_email = models.EmailField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '{} at {}'.format(self.title, self.company_name)


class JobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'
        exclude = ['approved']


class Event(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField()
    fb_id = models.CharField(max_length=300, default='')

    def __str__(self):
        return '{} at {}'.format(self.title, self.location)


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    list_position = models.IntegerField()

    def __str__(self):
        return self.question


class Gallery(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    full_size_image = models.ImageField(null=True)
    thumbnail_image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=300, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        pil_image_obj = Image.open(self.full_size_image)
        new_image = resizeimage.resize_width(pil_image_obj, 240)

        new_image_io = BytesIO()
        new_image.save(new_image_io, format='JPEG')

        temp_name = self.full_size_image.name

        self.thumbnail_image.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )

        super(GalleryImage, self).save(*args, **kwargs)
