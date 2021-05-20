from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Talk(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    speaker = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.JSONField(default=list)

    class Meta:
        verbose_name = "talk"
        verbose_name_plural = "talks"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("talk_detail", kwargs={"pk": self.pk})
