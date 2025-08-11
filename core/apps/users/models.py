from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils.models import TimeStampModelMixin, AuditModelMixin, SoftDeleteModelMixin, UserManager

class User(SoftDeleteModelMixin, TimeStampModelMixin, AuditModelMixin, AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    activity_level = models.CharField(
        max_length=20,
        choices=[
            ('sedentary', 'Sedentary'),
            ('light', 'Lightly Active'),
            ('moderate', 'Moderately Active'),
            ('active', 'Very Active'),
            ('extreme', 'Extremely Active'),
        ],
        blank=True
    )
    goal = models.CharField(
        max_length=20,
        choices=[
            ('maintain', 'Maintain Weight'),
            ('lose', 'Lose Weight'),
            ('gain', 'Gain Weight'),
        ],
        default='maintain'
    )
    is_active = models.BooleanField(default=True, db_index=True)
    
    def __str__(self):
        return self.username 
    
    objects = UserManager()
    all_objects = models.Manager()
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
