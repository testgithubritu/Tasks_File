from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user=models.CharField(max_length=200)
    learning=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    involvement=models.CharField(max_length=200)
    image=models.ImageField(upload_to='usermedia')


    def __str__(self):
        return '{}'.format(self.user)

class Education(models.Model):
    teaching=models.CharField(max_length=200)
    IT=models.CharField(max_length=200)
    engineering=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.teaching)


class link(models.Model):

    link=models.URLField(max_length=200)


    def __str__(self):
        return '{}'.format(self.link)

