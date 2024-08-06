from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name