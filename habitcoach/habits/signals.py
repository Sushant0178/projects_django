from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Habit, HabitRecord

@receiver(post_save, sender=Habit)
def create_today_record(sender, instance, created, **kwargs):
    if created:
        today = timezone.now().date()
        HabitRecord.objects.get_or_create(habit=instance, date=today)
