from django import forms
class PostForm(forms.Form):
    title=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'class':'form-control'}))
    where=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'class':'form-control'}))
    detail=forms.CharField(max_length=150)
    