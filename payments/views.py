from django.views.generic import FormView
from django.views.generic import TemplateView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render, get_object_or_404, redirect
from subscriptions.forms import SubsciptionForm
from videos.models import Video
from .models import Product
from django.conf import settings
import uuid
from django.contrib.auth.decorators import login_required
import json
from .utils import process_pdt
from django.views.decorators.http import  require_GET
from payments.models import Purchase
import ast
from django.contrib.auth.models import User
from subscriptions.models import Subscription
from django.utils.timezone import make_aware
from users.models import Profile
from dateutil.relativedelta import *
from datetime import datetime

@login_required()
def checkout(request):
    if request.method == "POST":
        subscription_form = SubsciptionForm(request.POST)

        if subscription_form.is_valid():
            subscription_type = subscription_form.cleaned_data["subscription"]
            user = request.user
            product = get_object_or_404(Product, name=subscription_type)
            
            initial_dict = {
                    "business": settings.PAYPAL_RECEIVER_EMAIL ,
                    "amount": product.price,
                    "currency_code": "USD",
                    "item_name": product.name,
                    "invoice": f"{uuid.uuid4()}",
                    "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
                    "return_url": request.build_absolute_uri(reverse('paypal_pdp_return')),
                    "cancel_return":request.build_absolute_uri(reverse('paypal-cancel')),
                    "lc": 'EN',
                    "no_shipping": '1',
                    "custom":json.dumps({
                            "user_id":user.id, 
                            "product_name":product.name,
                            "single_purchase":"False"
                    })
              
            }

            form = PayPalPaymentsForm(initial=initial_dict)

            context = {
                "form":form,
                "item_name":product.name,
                "item_price":product.price
            }
            return render(request, "payments/payment_form.html", context=context)


class PaypalCancelView(TemplateView):
    template_name = 'payments/payment_cancel.html'



@require_GET
def pdt_processor(request):
    pdt_obj, failed = process_pdt(request)
 
    context = {"failed": failed, "pdt_obj": pdt_obj}

    custom = ast.literal_eval(request.GET.get("custom"))

    # if this was a subscription redirect to success page
    if custom["single_purchase"] == "False":
            # run this is user subscribing

            user_id = custom["user_id"]
            product_name = custom["product_name"]

            
            
            # get the user from the id so that we can get the profile
            user = User.objects.get(id=user_id)
            profile,_ = Profile.objects.get_or_create(user=user)
            product = Product.objects.get(name=product_name)

            subscription_type = "monthly"

            # determine subscription type
            if product.expiration_duration == 3:
                subscription_type = "three_months"
            elif product.expiration_duration == 6:
                subscription_type = "six_months"
            elif product.expiration_duration == 12:
                subscription_type = "yearly"


            if not profile.subscription:
                # if this is the first time
                subscription = Subscription.objects.create(expiration=make_aware(datetime.now() + relativedelta(months=+product.expiration_duration)), subscription_type=subscription_type)
                profile.subscription = subscription
                
                profile.save()
            
            else:
                # if this is not the first time user is subscribing
                profile.subscription.expiration =  make_aware(datetime.now() + relativedelta(months=+product.expiration_duration))
                profile.subscription.subscription_type = subscription_type
                profile.subscription.save()
            return redirect(reverse('paypal-return'))

    if not failed:
    
        video_id = custom["video_id"]
        video = Video.objects.get(pk=video_id)
        
        # create a purchase
        Purchase.objects.create(resource=video, purchaser=request.user, tx=request.GET.get("tx"))

        context["video_id"]= video_id

        return render(request, 'payments/payment_pdp_success.html', context)
        
    else:
      
        return render(request, 'payments/error.html', context)

