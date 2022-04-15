from django import forms


class CartAddItem(forms.Form):
    def __init__(self, *args, **kwargs):
        self.sizes = kwargs.pop('size_choice') if 'size_choice' in kwargs else ()
        self.colors = kwargs.pop('color_choice') if 'color_choice' in kwargs else ()
        self.av_qnt = kwargs.pop('av_qnt') if 'av_qnt' in kwargs else ()
        super(CartAddItem, self).__init__(*args, **kwargs)
        self.fields['size'].choices = self.sizes
        self.fields['color'].choices = self.colors
        self.fields['quantity'].choices = self.av_qnt
        self.fields['size'].widget.attrs['class'] = 'selection'
        self.fields['color'].widget.attrs['class'] = 'selection'
        self.fields['quantity'].widget.attrs['class'] = 'selection'

    size = forms.ChoiceField(choices=())
    color = forms.ChoiceField(choices=())
    quantity = forms.TypedChoiceField(choices=(), coerce=int)
    update_quantity = forms.BooleanField(required=False,
                                         initial=False,
                                         widget=forms.HiddenInput
                                         )
