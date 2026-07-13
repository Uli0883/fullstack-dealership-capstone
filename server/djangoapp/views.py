from django.shortcuts import render, redirect, get_object_or_404
from .models import Dealer, DealerReview
from datetime import datetime

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'dealer_list.html', {'dealers': dealers})

def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    return render(request, 'dealer_detail.html', {'dealer': dealer})

def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    return render(request, 'add_review.html', {'dealer_id': dealer_id})

def submit_review(request):
    if request.method == 'POST':
        dealer_id = request.POST.get('dealer_id')
        dealer = get_object_or_404(Dealer, id=dealer_id)

        purchase_date_str = request.POST.get('purchase_date')
        purchase_date = datetime.strptime(purchase_date_str, '%Y-%m-%d').date()

        DealerReview.objects.create(
            dealer=dealer,
            reviewer_name=request.POST.get('reviewer_name'),
            review_text=request.POST.get('review_text'),
            rating=int(request.POST.get('rating')),
            car_make=request.POST.get('car_make'),
            car_year=int(request.POST.get('car_year')),
            purchase_date=purchase_date
        )
        return redirect('dealer_detail', dealer_id=dealer_id)
    return redirect('dealer_list')