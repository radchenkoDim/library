from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    def natural_key(self):
        return self.name
    

class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    def natural_key(self):
        return self.name


class Book(models.Model):
    num = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    cover = models.ImageField(upload_to="covers", blank=True, null=True)
    category = models.ForeignKey(
        Category, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="books")
    year = models.CharField(max_length=255, blank=True, null=True)
    tom = models.CharField(max_length=255, default="1")
    quantity = models.IntegerField(default=1)
    publisher = models.ForeignKey(
        Publisher, 
        blank=True,
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="books")
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.num}. {self.title}"
    
    def free_quantity(self):
        return self.quantity - self.takingbook_set.filter(return_date__isnull=True).count()