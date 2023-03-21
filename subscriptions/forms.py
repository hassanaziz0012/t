from django import forms


class SubsciptionForm(forms.Form):
    subscription = forms.ChoiceField(choices=(("monthly", "monthly"), ("three_months", "three_months"),("six_months", "six_months"), ("yearly", "yearly")))