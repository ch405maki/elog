from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    middle_name = forms.CharField(max_length=100, required=False, label="Middle Name")
    dob_year = forms.IntegerField(required=False, label="Date of Birth (Year)")
    dob_month = forms.IntegerField(required=False, label="Date of Birth (Month)")
    dob_day = forms.IntegerField(required=False, label="Date of Birth (Day)")
    gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")], required=False)
    student_id = forms.CharField(max_length=50, required=False)
    street_address1 = forms.CharField(max_length=255, required=False)
    street_address2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    state_prov = forms.CharField(max_length=100, required=False)
    zip_code = forms.CharField(max_length=20, required=False)
    mobile = forms.CharField(max_length=15, required=False)
    course = forms.CharField(max_length=100, required=False)
    year = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Save Profile info
        profile = Profile(
            user=user,
            middle_name=self.cleaned_data['middle_name'],
            dob_year=self.cleaned_data['dob_year'],
            dob_month=self.cleaned_data['dob_month'],
            dob_day=self.cleaned_data['dob_day'],
            gender=self.cleaned_data['gender'],
            student_id=self.cleaned_data['student_id'],
            street_address1=self.cleaned_data['street_address1'],
            street_address2=self.cleaned_data['street_address2'],
            city=self.cleaned_data['city'],
            state_prov=self.cleaned_data['state_prov'],
            zip_code=self.cleaned_data['zip_code'],
            mobile=self.cleaned_data['mobile'],
            course=self.cleaned_data['course'],
            year=self.cleaned_data['year'],
        )
        profile.save()
        return user
