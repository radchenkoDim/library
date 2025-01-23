from django.db import models # type: ignore
from datetime import datetime

# Create your models here.
class TakingBook(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    take_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.book} - {self.take_date}"
    

class WantBook(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    where = models.CharField(max_length=255)
    votes = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.title}"
    

class Vote(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    want_book = models.ForeignKey(WantBook, on_delete=models.CASCADE)
    voted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.want_book}"