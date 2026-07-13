from django.contrib import admin
from .models import Dealer, DealerReview

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'state', 'zip')
    search_fields = ('name', 'city', 'state')

@admin.register(DealerReview)
class DealerReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'dealer', 'reviewer_name', 'rating', 'car_make', 'car_year')
    list_filter = ('rating', 'dealer')