from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'overall_satisfaction', 'product_quality', 'delivery_service_rating', 'recommendation', 'terms_agreed', 'created_at')
    list_filter = ('overall_satisfaction', 'recommendation', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
