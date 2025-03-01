from django.shortcuts import render
from django.contrib.auth.decorators import staticmethod

# Create your views here.

@staticmethod
    def can_create(user):
        return user.is_staff

    def can_delete(self, user):
        if user.is_staff:
            return True
        return False
