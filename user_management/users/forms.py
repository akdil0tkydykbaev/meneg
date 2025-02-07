# forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'number', 'direction', 'is_deleted', 'connected']  # добавьте остальные поля

    # Вы можете установить отображение поля выбора, если необходимо.
    direction = forms.ChoiceField(choices=User.IT_DIRECTIONS, required=True)

