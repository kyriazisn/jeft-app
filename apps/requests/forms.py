from decimal import Decimal

from django import forms

from .models import GiftRequest


class GiftRequestForm(forms.ModelForm):
    class Meta:
        model = GiftRequest
        fields = ("title", "description", "category", "requested_url", "max_amount")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. 27-inch gaming monitor"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe the item you are requesting."}),
            "category": forms.TextInput(attrs={"placeholder": "e.g. Technology"}),
            "requested_url": forms.URLInput(attrs={"placeholder": "Optional product link"}),
            "max_amount": forms.NumberInput(attrs={"min": "1", "max": "500", "step": "0.01"}),
        }

    def clean_max_amount(self):
        amount = self.cleaned_data["max_amount"]
        if amount <= 0:
            raise forms.ValidationError("The maximum amount must be greater than zero.")
        if amount > Decimal("500.00"):
            raise forms.ValidationError("The maximum amount cannot exceed €500.")
        return amount

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        forbidden_terms = ("weapon", "explosive", "illegal drug")
        if any(term in description.lower() for term in forbidden_terms):
            raise forms.ValidationError("This request contains content that cannot be submitted.")
        return description
