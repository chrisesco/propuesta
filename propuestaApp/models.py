from django.db import models

# Create your models here.


class Aspirante(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    semester = models.IntegerField()
    degree = models.CharField(max_length=120)
    institute = models.CharField(max_length=120)


    class Meta:
        verbose_name = "Aspirante"
        verbose_name_plural = "Aspirantes"

    def __str__ (self) -> str:
        return f'Nombre: {self.first_name}, Apellidos: {self.last_name}, Universidad: {self.institute}'

    
class Habilidad(models.Model):
    name_skill =  models.CharField(max_length=50)
    description_skill = models.CharField(max_length=320)
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)

    def __str__(self) ->str:
        return f'{self.name_skill},{self.description_skill}'


    

