from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils.models import TimeStampModelMixin, AuditModelMixin, SoftDeleteModelMixin, UserManager

class User(SoftDeleteModelMixin, TimeStampModelMixin, AuditModelMixin, AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'
        NOT_SAY = 'N', 'Prefer not to say'
    
    class ActivityLevel(models.TextChoices):
        SEDENTARY = 'sedentary', 'Sedentary'
        LIGHT = 'light', 'Lightly Active'
        MODERATE = 'moderate', 'Moderately Active'
        ACTIVE = 'active', 'Very Active'
        EXTREME = 'extreme', 'Extremely Active'
    
    class Goal(models.TextChoices):
        MAINTAIN = 'maintain', 'Maintain Weight'
        LOSE = 'lose', 'Lose Weight'
        GAIN = 'gain', 'Gain Weight'
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    activity_level = models.CharField(
        max_length=20,
        choices=ActivityLevel.choices,
        blank=True
    )
    goal = models.CharField(
        max_length=20,
        choices=Goal.choices,
        default=Goal.MAINTAIN
    )
       
    objects = UserManager()
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username
