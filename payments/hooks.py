from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
from users.models import Profile
from payments.models import Product
from subscriptions.models import Subscription
from django.contrib.auth.models import User
from dateutil.relativedelta import *
from datetime import datetime
import ast
from django.utils.timezone import make_aware

@receiver(valid_ipn_received)
def user_paid(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # Not a valid payment
            return

        # Undertake some action depending upon `ipn_obj`.
   
        custom_info = ast.literal_eval(ipn_obj.custom)

        if custom_info["single_purchase"] == "False":
            # run this is user subscribed 

            user_id = custom_info["user_id"]
            product_name = custom_info["product_name"]

            
            
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
    
    else:
        pass
