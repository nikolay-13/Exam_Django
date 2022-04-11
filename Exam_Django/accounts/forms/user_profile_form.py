import re

from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm

from Exam_Django.accounts.models.models import Profile

UserModel = get_user_model()


class UserProfileCreationForm(UserCreationForm):
    _MAX_WIDTH = 100
    _MAX_HEIGHT = 100
    _pattern = r'^[A-z]*$'
    _Name_length_msg = ' must be at least two characters.'
    _Name_Character_Msg = ' must contain only letters.'
    _TEL_MESSAGE = 'Make sure you entered a valid number.'
    _TEL_MESSAGE_UNIQUE = 'User with this number already exists.'
    profile_picture = forms.ImageField()
    first_name = forms.CharField(
        max_length=30,
    )
    last_name = forms.CharField(
        max_length=30
    )
    tel_number = forms.CharField(
        max_length=10,
    )

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        super(UserProfileCreationForm, self).clean()
        first_name = self.cleaned_data['first_name']
        if 2 > len(first_name):
            msg = 'First name' + self._Name_length_msg
            self._errors['first_name'] = self.error_class([msg])
        if not re.match(self._pattern, first_name):
            msg = 'First name' + self._Name_Character_Msg
            self._errors['first_name'] = self.error_class([msg])
        return first_name

    def clean_last_name(self):
        super(UserProfileCreationForm, self).clean()
        last_name = self.cleaned_data['last_name']
        if 2 > len(last_name):
            msg = 'Last name' + self._Name_length_msg
            self._errors['last_name'] = self.error_class([msg])
        if not re.match(self._pattern, last_name):
            msg = 'Last name' + self._Name_Character_Msg
            self._errors['last_name'] = self.error_class([msg])
        return last_name

    def clean_tel_number(self):
        super(UserProfileCreationForm, self).clean()
        number = Profile.objects.only('tel_number').filter(tel_number=self.cleaned_data['tel_number'])
        tel_number = self.cleaned_data['tel_number']
        if not re.match(r'^[0-9]{10}$', tel_number):
            msg = self._TEL_MESSAGE
            self._errors['tel_number'] = self.error_class([msg])
        if number:
            msg = self._TEL_MESSAGE_UNIQUE
            self._errors['tel_number'] = self.error_class([msg])
        tel_number = tel_number
        return tel_number

    def save(self, commit=True):
        user_p = super().save(commit=commit)

        Profile.objects.create(
            profile_picture=self.cleaned_data['profile_picture'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            tel_number=self.cleaned_data['tel_number'],
            user=user_p,
        )
        return user_p


class UserLogInForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that password was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            'user',
        )

    email = forms.EmailField()


