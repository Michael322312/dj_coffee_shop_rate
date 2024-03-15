from django import forms
from review_system.models import Review

class ReviewForm(forms.Form):
    class Meta:
        model = Review
        exclude = ["user", "pub_date"]