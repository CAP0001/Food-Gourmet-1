from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    orders_count = models.PositiveIntegerField(default=0) 
    
    def get_status(self): 
        if self.orders_count >= 50:
            return {'name': 'DIAMOND MEMBER', 'class': 'diamond'}
        elif self.orders_count >= 35:
            return {'name': 'Lapiz member', 'class': 'lapiz'}
        elif self.orders_count >= 20:
            return {'name': 'Golden member', 'class': 'gold'}
        elif self.orders_count >= 10:
            return {'name': 'Silver member', 'class': 'silver'}
        elif self.orders_count >= 5:
            return {'name': 'Bronze member', 'class': 'bronze'}
        return None # Добавил возврат None для обычных юзеров

    def __str__(self):
        return f'User profile {self.user.username}'

class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Изменил на FloatField, чтобы средний рейтинг мог быть 4.5
    stars = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5.0
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Review by {self.user.username} on {self.food.name}"