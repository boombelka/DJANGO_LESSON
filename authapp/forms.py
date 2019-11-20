from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import forms
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):     # создание функции изменения возраста.
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return data
"""
часть урока с регистрацией. и созданием форм автоматизированно.
"""
#    def __init__(self, *args, **kwargs):
#    super(ShopUserLoginForm, self).__init__(*args, **kwargs)
#        for field_name, field in self.fields.items():
#        field.widget.attrs['class'] = 'form-control'

