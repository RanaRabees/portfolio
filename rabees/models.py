from django.db import models

# Create your models here.


class Userdata(models.Model):
    username = models.CharField(max_length=50, default="")
    useremail = models.EmailField(max_length=50, default="")
    usermessage = models.CharField(max_length=50, default="")
    # useremail               = models.CharField(max_length=50 ,default="")
    # photo = models.ImageField(upload_to="myimage")
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
