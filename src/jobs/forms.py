from django import forms
from .models import Job, Bid


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['employer'].widget = forms.HiddenInput()

    class Meta:
        model = Job
        exclude = ('id',)


class BidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BidForm, self).__init__(*args, **kwargs)
        self.fields['freelancer'].widget = forms.HiddenInput()
        self.fields['job'].widget = forms.HiddenInput()

    class Meta:
        model = Bid
        fields = ['job', 'freelancer', 'amount', 'description', 'additional_description']
