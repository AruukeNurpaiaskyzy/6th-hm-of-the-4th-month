from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    cause = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Заявка от {self.name}"
    
    class Meta :
        verbose_name = ""
        verbose_name_plural = "Заявки"
class Main(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='main/')
    titlemaking = models.CharField(max_length=255)
    descriptionmaking = models.TextField() 
    image_making = models.ImageField(upload_to='making/')
    titleparadise = models.CharField(max_length=255)
    titlexperiences = models.CharField(max_length=255)
    titletrips = models.CharField(max_length=255)
    descriptiontrips = models.TextField() 
    titletravels = models.CharField(max_length=255)
    descriptiontravels = models.TextField() 
    titleblog = models.CharField(max_length=255)
    titlestaff = models.CharField(max_length=255)
    titlepartners = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name = ""
        verbose_name_plural = "Настройка главной страницы"

class Forms(models.Model):
    titleimg = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='forms',
         verbose_name='Фото'
     )

    def __str__(self):
        return self.titleimg
    
    class Meta:
        verbose_name_plural = 'Форма'

class Trips(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='forms',
         verbose_name='Фото'
     )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Трипы'
class Forms2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='forms2',
         verbose_name='Фото'
     )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Формы2'
class Forms3(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='forms3',
         verbose_name='Фото'
     )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Формы3'
class Minilogo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='minilogo',
         verbose_name='Фото'
     )
    
    class Meta:
        verbose_name_plural = 'minilogos'
class Stuffs(models.Model):
    role = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='stuffs',
         verbose_name='Фото'
     )
    
    class Meta:
        verbose_name_plural = 'stuffs'


class Logo(models.Model):
    image = models.ImageField(
         upload_to='logo',
         verbose_name='Фото'
     )
    
    class Meta:
        verbose_name_plural = 'logos'
class Forms4(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(
         upload_to='forms4',
         verbose_name='Фото'
     )

    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name_plural = 'Формы4'
        

