from django.db import models

RECOMMENDATION_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Other', 'Other'),
]

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    overall_satisfaction = models.CharField(max_length=10)  # 'happy', 'neutral', 'sad'
    product_quality = models.IntegerField()  # 1 to 5
    delivery_service_rating = models.IntegerField()  # 1 to 10
    
    recommendation = models.CharField(max_length=10, choices=RECOMMENDATION_CHOICES)
    additional_feedback = models.TextField(blank=True)
    terms_agreed = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
