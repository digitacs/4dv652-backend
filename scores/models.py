from django.db import models


# Create your models here.
class Score(models.Model):
    Id = models.UUIDField(primary_key=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now_add=True)
    Value = models.FloatField()

    class Meta:
        db_table = "Score"
        ordering = ['CreatedAt']

    def __str__(self):
        return self.Value
