from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['tittle', 'description', 'image_url']
        labels = {
            'tittle': 'Título',
            'description': 'Descrição',
            'image_url': 'URL da imagem',
        }
        widgets = {
            'tittle': forms.TextInput(attrs={'placeholder': 'Digite o título do filme'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva o filme'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://exemplo.com/imagem.jpg'}),
        }
