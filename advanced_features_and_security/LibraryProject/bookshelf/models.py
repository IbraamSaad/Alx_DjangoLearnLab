from django.db import models

# Create your models here.

lass CustomUser(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)

    def __str__(self):
        return self.username
        
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	publication_year = models.IntegerField()
