from django.db import models
from django.contrib.auth.models import User

class Deal(models.Model):
    name = models.CharField(max_length = 180)
    website = models.CharField(max_length = 180)
    image = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, max_length=100)
    description = models.CharField(max_length = 500, blank = True)
    status = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name