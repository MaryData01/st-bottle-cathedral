import os
from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)

    def __str__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    graphic = models.ImageField(upload_to='series/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    passage = models.CharField(max_length=200, blank=True)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True, related_name='sermons')
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True, related_name='sermons')
    
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="YouTube or Vimeo URL")
    livestream_url = models.URLField(blank=True, help_text="YouTube Live Embed URL if applicable")
    transcript = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
