from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    table_of_contents = models.TextField()
    highlights = models.TextField()
    methodology = models.TextField()
    price = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
