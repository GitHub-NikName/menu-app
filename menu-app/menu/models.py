from django.db import models
from django.urls import reverse
from django.http import Http404


class Menu(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительская категория',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    position = models.IntegerField(verbose_name='Позиция', blank=True,
                                   null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True, null=True,
                                 unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_named_url = reverse(url_name, args=params)
            if self.url:
                if self.url != reversed_named_url:
                    raise Http404('url does not match named_url')
            else:
                self.url = reversed_named_url
        super(Menu, self).save(*args, **kwargs)
