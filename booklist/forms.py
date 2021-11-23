from django.forms import ModelForm
from .models import BookList

class BookListForm(ModelForm):
    class Meta:
        model = BookList
        fields = '__all__'
        