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
        return None 

    def __str__(self):
        return f'User profile {self.user.username}'

class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    stars = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5.0
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    food_type = models.CharField(max_length=200, default='Other')
    country = models.CharField(max_length=200, default='innational')

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

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.food.name} x {self.quantity} for {self.user.username}"