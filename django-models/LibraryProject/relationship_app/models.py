from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=70)
    books = models.ManyToManyField(Book, related_name='library')
    def __str__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=70)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    USER_ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
