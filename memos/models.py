from django.db import models

# Create your models here.

class Memos(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.CharField(max_length=50)

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 30:
            return self.content[:30] + "..."
        return self.content
