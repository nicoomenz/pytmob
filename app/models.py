from django.db import models
from django.db.models.signals import post_save
from django.core.cache import cache

class Redirect (models.Model):
    key = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Meta:
    verbose_name="Redirect"
    ordering=['key']

def signal_update(sender, instance, **kwars):    
    if instance.active:
        cache.set(instance.key, instance)
    else:
        cache.delete(instance.key)

post_save.connect(signal_update, sender = Redirect)