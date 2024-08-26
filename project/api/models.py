from django.db import models

  
class MovieModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    
    class Meta:
        verbose_name = "MovieModel"
        verbose_name_plural = "MovieModels"
    
    def _str_(self):
        return self.title