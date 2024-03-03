from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripción', max_length=110, blank=False, null=False)
    contents = RichTextField(verbose_name = "Contenido del post")
    image = models.ImageField(verbose_name = 'Imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de Actualización')
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
        
    def __str__(self) -> str:
        return self.title
    