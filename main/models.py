from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_photo/')


class Services(models.Model):
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='services_photo/')


class About(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='about/')


class Portfolio(models.Model):
    img = models.ImageField(upload_to='portfolio/')


class Testimonial(models.Model):
    user_name = models.CharField(max_length=255)
    text = models.TextField()


class Client(models.Model):
    brand_photo = models.ImageField(upload_to='brand/')


class Contact (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
