from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [('M', '雄性'), ('F', '雌性')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_vaccinated = models.BooleanField(default=False)
    is_neutered = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pets/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_gender_display(self):
        return dict(self.GENDER_CHOICES).get(self.gender, '')
