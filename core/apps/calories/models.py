from django.db import models
from django.conf import settings
from core.utils.models import SoftDeleteModelMixin, TimeStampModelMixin, AuditModelMixin


class CalorieRecord(SoftDeleteModelMixin, TimeStampModelMixin, AuditModelMixin):
    class MealType(models.TextChoices):
        BREAKFAST = 'breakfast', 'Breakfast'
        LUNCH = 'lunch', 'Lunch'
        DINNER = 'dinner', 'Dinner'
        SNACK = 'snack', 'Snack'
        OTHER = 'other', 'Other'
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='calorie_records'
    )
    date = models.DateField(db_index=True)
    meal_type = models.CharField(
        max_length=20,
        choices=MealType.choices,
        default=MealType.OTHER
    )
    food_name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    
    
    class Meta:
        indexes = [models.Index(fields=['user', 'date'])]

    def __str__(self):
        return f"{self.food_name}({self.calories} kcal) by {self.user.username}"