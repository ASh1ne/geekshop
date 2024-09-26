from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from authapp.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2','age','image')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес электронной почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['image'].widget.attrs['placeholder'] = 'Загрузите фото'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_age(self):
        user_age = self.cleaned_data['age']
        if user_age <= 25:
            raise forms.ValidationError('Вам необходимо подрасти!')

        return user_age

    def clean_password1(self):
        my_pass1=self.cleaned_data['password1']
        if len(my_pass1) <= 2:
            raise forms.ValidationError('Удлинните пароль!')
        return my_pass1

    def clean_password2(self):
        my_pass2=self.cleaned_data['password2']
        if my_pass2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Пароли не совпадают!')
        return

class UserProfilerForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(),required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'age','image')

    def __init__(self, *args, **kwargs):
        super(UserProfilerForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    def clean_age(self):
        user_age = self.cleaned_data['age']
        if user_age <= 25:
            raise forms.ValidationError('Вам необходимо подрасти!')
        return user_age