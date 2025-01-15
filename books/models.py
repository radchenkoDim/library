from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"

    def natural_key(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=255)
 
    class Meta:
        unique_together = ["name", "category"]

    def __str__(self):
        return f"{self.name}"

    def natural_key(self):
        return self.name

class Book(models.Model):
    num = models.IntegerField()
    title = models.CharField(max_length=255, default="No data")
    author = models.CharField(max_length=255, default="No data")
    category = models.ForeignKey(
        Category, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="books",
        default="No data")
    subcategory = models.ForeignKey(
        Subcategory, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="books",
        default="-")
    year = models.CharField(max_length=255, default="No data")
    tom = models.CharField(max_length=255, default="No data")
    publisher = models.CharField(max_length=255, default="No data")
    notes = models.CharField(max_length=255, default="No notes")

    def __str__(self):
        return f"{self.num}. {self.title}"