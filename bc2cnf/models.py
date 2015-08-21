from django.db import models
from django.forms import ModelForm
import random
import string
# Create your models here.
N=4
class Submission(models.Model):
#	datetime=models.DateTimeField()
        userid=models.CharField(max_length=8, blank=False, null=False, default=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)))
	bcfile=models.FileField(upload_to='', blank=False, null=False)

class SubmissionForm(ModelForm):
	class Meta:
		model = Submission
		fields = ['userid','bcfile']
