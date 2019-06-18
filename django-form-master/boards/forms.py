from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    #  Model 의 대한 정보들 입력
    class Meta:
        model = Board
        fields = ('title', 'content', )
