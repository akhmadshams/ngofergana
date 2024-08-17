from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField


class NNTName(models.Model):
    name = models.CharField(max_length=500, verbose_name='NNT nomi')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'NNT Nomlari'


class NTT(models.Model):
    nnt = models.ForeignKey(NNTName, on_delete=models.CASCADE, verbose_name='NNT')
    image = models.ImageField(upload_to='ntt/director', verbose_name='NNT rahbarini rasmi')
    name = models.CharField(max_length=550, verbose_name='NNT nomi')
    director = models.CharField(max_length=255, verbose_name='Direktor FISH')
    register_number = models.CharField(max_length=550, verbose_name='Royxatdan otgan raqami')
    membership = models.CharField(max_length=550, verbose_name='Azoligi')
    purpose = models.TextField(verbose_name='Maqsadi')
    direction = models.TextField(verbose_name='Yonalishi')
    projects = models.TextField(verbose_name='Loyihalari')
    address = models.TextField(verbose_name='Manzil va tel raqam')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'NNT Tashkilotlari'


class CityName(models.Model):
    name = models.CharField(max_length=255, verbose_name='Shaxar, tuman nomi')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tuman shaxar nomlari'


class Streets(models.Model):
    city = models.ForeignKey(CityName, on_delete=models.CASCADE, verbose_name='Shaxar tuman nomini tanlang')
    # name = models.CharField(max_length=255, verbose_name='MFY nomi')
    population = models.CharField(max_length=255, verbose_name='Aholi soni')
    mfy_count = models.CharField(max_length=255, verbose_name='MFY lar soni')
    area = models.CharField(max_length=255, verbose_name='Hududi')

    def __str__(self):
        return self.city.name

    class Meta:
        verbose_name_plural = 'MFY haqida'


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    body = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Yangiliklar'


class Grant(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    body = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField()

    def save(self, *args, **kwargs):
        super(Grant, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Grantlar'


class NormativHujjat(models.Model):
    number = models.CharField(max_length=255)
    title = models.TextField()
    link = models.CharField(max_length=550)
    year = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Normativ Hujjatlar'


class OAV(models.Model):
    CHOICES = (
        ('TV', 'TV'),
        ('Gazeta', 'Gazeta'),
        ('Jurnal', 'Jurnal'),
    )
    choice_field = models.CharField(max_length=20, choices=CHOICES)
    name = models.CharField(max_length=255)
    body = RichTextField()

    def __str__(self):
        return f"{self.choice_field}: {self.name}"

    class Meta:
        verbose_name_plural = 'OAV'


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}   |   {self.phone}"

    class Meta:
        verbose_name_plural = 'Xabarlar'


class Index(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TextModel(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
