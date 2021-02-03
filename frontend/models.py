from django.db import models

# Create your models here.

class Biography(models.Model):
    bio_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/')
    bio_title= models.CharField(max_length=100, verbose_name='Profile Title')
    # bio_price= models.PositiveIntegerField()
    bio_description = models.TextField(verbose_name='Description')

    class Meta():
        verbose_name_plural = 'Biography'

    def __str__(self):
        return self.bio_title