from django import forms
class ProductInsertForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product ID:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your ID'
            }
        )
    )
    product_name = forms.CharField(
        label='Enter Product Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color = forms.CharField(
        label='Enter Product Color:',
        widget=forms.TextInput(
             attrs={
                'class':'form-control',
                'placeholder':'Product Color'
             }
        )
    )
    product_class = forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
class ProductUpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
class ProductDeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'fprm-control',
                'placeholder':'Product ID'
            }
        )
    )
