from django.db import models

# Create your models here.


class Label(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    origin_country = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    year_of_creation = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Song(models.Model):

    CHOICES_GENRES = (
        ('C', 'Crossbreed'),
        ('D', 'Drumstep'),
        ('J', 'Jump up'),
        ('L', 'Liquid'),
        ('N', 'Neurofunk'),
        ('O', 'Other')
    )

    title = models.CharField(max_length=30)
    features = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=1, choices=CHOICES_GENRES)
    release_date = models.DateField()
    duration = models.DecimalField(max_digits=5, decimal_places=2, help_text="in Minutes")
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True)
    producer = models.ManyToManyField('Musician', related_name='songs', blank=True)

    def __str__(self):
        return self.title

class Musician(models.Model):

    alias = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    year_of_birth = models.IntegerField()
    label = models.ManyToManyField('Label', related_name='producer', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.alias