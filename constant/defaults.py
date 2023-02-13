from models import timezone

workweek_morning = timezone.Timezone('00:01', '09:00', 25)
workweek_noon = timezone.Timezone('09:01', '18:00', 15)
workweek_nights = timezone.Timezone('18:01', '00:00', 20)
work_weekend_morning = timezone.Timezone('00:01', '09:00', 30)
work_weekend_noon = timezone.Timezone('09:01', '18:00', 20)
work_weekend_nights = timezone.Timezone('18:01', '00:00', 25)
