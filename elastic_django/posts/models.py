from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(
        auto_now_add=False,
        auto_now=False,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return f'posts/{self.id}'

    @property
    def elastic_score(self):
        return 0.75
