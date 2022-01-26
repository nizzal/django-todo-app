from django.db import models
import uuid

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)

    def __str__(self):
        return str(
            [
                "Title: ",
                self.title,
                "is_edited:",
                self.is_edited,
                "is_finished:",
                self.is_finished,
            ]
        )
