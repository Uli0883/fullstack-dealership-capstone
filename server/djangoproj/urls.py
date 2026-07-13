from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView  # <--- Importar TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from djangoapp.views import dealer_list, dealer_detail, add_review, submit_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    path('', dealer_list, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/', http_method_names=['get']), name='logout'),
    path('dealer/<int:dealer_id>/', dealer_detail, name='dealer_detail'),
    path('add_review/<int:dealer_id>/', add_review, name='add_review'),
    path('submit_review/', submit_review, name='submit_review'),
]