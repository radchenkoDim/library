from django.db import models

# Create your models here.
class TakingBook(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    take_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.book} - {self.take_date}'