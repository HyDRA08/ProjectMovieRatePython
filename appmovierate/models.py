from django.db import models

# Create your models here.
morf=(
    ('Male','MALE'),
    ('Female','FEMALE'),
)
# sign up
class modelsignup(models.Model):
    name=models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    # gender = models.CharField(max_length=10)
    gender = models.CharField(choices=morf, max_length=10)
    user_name = models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    def __str__(self):
        return self.user_name


class modelmovie(models.Model):
    # movie_id=models.IntegerField(max_length=10)
    movie_name=models.CharField(max_length=30,default="")
    movie_director=models.CharField(max_length=30)
    movie_studio=models.CharField(max_length=40)
    # movie_studio=models.CharField(choices=studionames, max_length=40,default="")
    movie_year=models.CharField(max_length=10)
    movie_image=models.FileField(upload_to='images/',default="")
    def __str__(self):
        return self.movie_name

class modelrating(models.Model):
    movie_name=models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    ratings=models.IntegerField()
    review = models.CharField(max_length=255)
    date = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.user_name
