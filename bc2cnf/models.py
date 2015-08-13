from django.db import models

# Create your models here.
class Submission(models.Model):
	datetime=models.DateTimeField()
	bcfile=models.FileField(upload_to='bc2files')
