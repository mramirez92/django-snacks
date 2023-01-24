from django.urls import path
from .views import AboutView, HomePageView

urlpatterns = [
    # routes
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about')

]



