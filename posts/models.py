from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to = 'images/')