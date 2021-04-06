from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import Todo


class TodoCreateForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Todo
        fields = [
            'description',
            'priority',
        ]
