from django.urls import path, include
from . import views
urlpatterns = [
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
    path("checkout/", views.checkout, name="checkout"),
    path('download-video/', views.pdt_processor, name='paypal_pdp_return'),
]