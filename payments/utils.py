import string
from paypal.standard.pdt.forms import PayPalPDTForm
from paypal.standard.pdt.models import PayPalPDT
from paypal.utils import warn_untested
from datetime import datetime
from dateutil.parser import parse   

def process_pdt(request):
    """
    Payment data transfer implementation:
    https://developer.paypal.com/webapps/developer/docs/classic/products/payment-data-transfer/
    This function returns a tuple of (pdt_obj, failed)
    pdt_obj is an object of type PayPalPDT
    failed is a flag that is True if the input data didn't pass basic validation.
    Note: even for failed=False You must still check the pdt_obj is not flagged i.e.
    pdt_obj.flag == False
    """

    pdt_obj = None
    txn_id = request.GET.get("tx")
    failed = False

    if txn_id is not None:
        # If an existing transaction with the id tx exists: use it
        try:
            pdt_obj = PayPalPDT.objects.get(txn_id=txn_id)
        except PayPalPDT.DoesNotExist:
            # This is a new transaction so we continue processing PDT request

            pass

        if pdt_obj is None:
            # process the date format
            date = request.GET.get("payment_date")
           

            date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
            
            string_date = date.strftime("%H:%M:%S %b %m, %Y PDT")
            
            data = request.GET.copy()

            data["payment_date"] = string_date
            data['notify_version'] = 1


            form = PayPalPDTForm(data)
            if form.is_valid():

                try:
                    pdt_obj = form.save(commit=False)
                except Exception as e:
                    warn_untested()
                    error = repr(e)
                    failed = True
            else:
               
                warn_untested()
                error = form.errors
                failed = True

            if failed:
                warn_untested()
                pdt_obj = PayPalPDT()
                pdt_obj.set_flag(f"Invalid form. {error}")

            pdt_obj.initialize(request)

            if not failed:
                # The PDT object gets saved during verify
                pdt_obj.verify()
    else:
        pass  # we ignore any PDT requests that don't have a transaction id

    return (pdt_obj, failed)