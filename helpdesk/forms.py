from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

TIPO_USUARIO_CHOICES = (
    ('usuario', 'Usuário'),
    ('tecnico', 'Técnico'),
)

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Nome completo')
    tipo_usuario = forms.ChoiceField(
        choices=User.TIPO_USUARIO_CHOICES,
        widget=forms.RadioSelect,
        label="Tipo de conta",
        initial='usuario'
    )
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2', 'tipo_usuario')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))