from escritorio.models import Relatorio
from django import forms


class FileFieldForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FileFieldForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Relatorio
        fields = ("__all__")