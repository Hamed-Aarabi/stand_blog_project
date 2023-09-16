from django import forms
from .models import Article, Comment

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','author', 'image', 'body', 'tags', 'categorie', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.CheckboxInput(attrs={'class':'form-control'})
        }

