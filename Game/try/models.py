from django.db import models

# Create your models here.
class Game(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rule = models.TextField()
    link = models.URLField(null=True, blank=True)
    TYPE_CHOICES = [
        ('ETG', 'ETG'),
        ('SLOT', 'Slot'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='SLOT')

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='game_images/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Jurisdiction(models.Model):
    Jurisdiction_CHOICES = [
        ('MO', 'MACAU'),
        ('PH', 'PH-PAGCOR'),
        ('SE-ASIA', 'SE-asia'),
        ('US CA-TRIBAL', 'US CA-Tribal'),
        ('US FL-PARI', 'US FL-Pari'),
        ('US FL-SEMINOLE', 'US FL-Seminole'),
        ('US OKLA', 'US OKLA'),
        ('US OKLA-CHICKSAW', 'US OKLA-Chicksaw'),
        ('US OKLA-CHOCTAW', 'US OKLA-Choctaw'),
        ('US MISSISSPPI', 'US Mississppi'),
        ('US MS CHOCTAW', 'US MS Choctaw'),
        ('PUERTO RICO', 'Puerto Rico'),
        ('US ARKANSAS', 'US Arkansas'),
        ('US NORTH-DAKOTA', 'US North-Dakota'),
        ('US NEBRASKA', 'US Nebraska'),
    ]
    jurisdiction = models.CharField(max_length=100, choices=Jurisdiction_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.jurisdiction