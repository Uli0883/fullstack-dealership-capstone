from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)  # Cambiar de full_name a name
    short_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class DealerReview(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    car_make = models.CharField(max_length=50, blank=True, null=True)      # <-- opcional
    car_year = models.IntegerField(blank=True, null=True)                  # <-- opcional
    purchase_date = models.DateField(blank=True, null=True)                # <-- opcional

    def __str__(self):
        return f"{self.reviewer_name} - {self.dealer.name}"