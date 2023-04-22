from unicodedata import category
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     valid_extensions = ['.jpg', '.png']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('پسوند فایل نا معتبر هست! ')


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    title = models.CharField(max_length=32)
    cover = models.ImageField(blank=True, null = True, upload_to='blog/images/categories/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_OF_POST = (
        ('draft', 'پیش نویس'),
        ('published', 'منتشر شده'),
    )
    cover = models.FileField(blank=True, null = True, upload_to="blog/images/posts/%Y/%m/")
    title = models.CharField(verbose_name='عنوان', max_length=64)
    slug = models.SlugField(verbose_name='نامک', unique=True)
    intro = models.TextField(verbose_name='خلاصه')
    content = RichTextField(verbose_name='محتوا', config_name='awesome_ckeditor')
    category = models.ForeignKey(Category, verbose_name="دسته", related_name="post", on_delete=models.PROTECT)
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE, related_name='post')
    featured = models.BooleanField(default=False)
    status = models.CharField(verbose_name='وضعیت', max_length=10, choices=STATUS_OF_POST, default='draft')
    created_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = ("نوشته")
        verbose_name_plural = ("نوشته‌ها")

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        """Update URL for Post"""
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        """Delete URL for Post"""
        return reverse("post_delete", kwargs={"slug": self.slug})

    objects = models.Manager()
    published = PublishedManager()


# class Comment(models.Model):
#
#     class Meta:
#         ordering = ('-created_at',)
#         verbose_name = 'نظر'
#         verbose_name_plural = 'نظرات'
#
#     article = models.ForeignKey(Post, verbose_name='نوشته', related_name='comments', on_delete=models.CASCADE)
#     name = models.CharField(verbose_name='توسط', max_length=32)
#     email = models.EmailField(verbose_name='ایمیل')
#     created_at = models.DateTimeField(verbose_name='ارسال شده', auto_now_add=True)
#
#     def __str__(self):
#         return self.name

