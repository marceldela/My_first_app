from django import forms
from django.forms import TextInput

from excel.models import Station, Package, PeriodYear, PeriodMonth, IndexPackage


class CreateStationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'



class CreatePackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = "__all__"

class CreatePeriodYearForm(forms.ModelForm):
    class Meta:
        model = PeriodYear
        fields = "__all__"

class CreatePeriodMonthForm(forms.ModelForm):
    class Meta:
        model = PeriodMonth
        fields = "__all__"



class CreateIndexPackageForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['period_year'].queryset = PeriodYear.objects.order_by('Station')
    class Meta:
        model = IndexPackage
        fields = '__all__'


class CalculateFormMin(forms.Form):
    package = forms.ModelChoiceField(queryset=Package.objects.order_by('station'), label='Pakiet')
    year_period = forms.ModelChoiceField(queryset=PeriodYear.objects.order_by('Station'), label='Budżet roczny')
    month_period = forms.ModelChoiceField(queryset=PeriodMonth.objects.order_by('station'), label='Miesiąc')
    index = forms.FloatField(label='Index dopasowania')

class CalculateFormMax(forms.Form):
    package = forms.ModelChoiceField(queryset=Package.objects.order_by('station'), label='Pakiet')
    year_period = forms.ModelChoiceField(queryset=PeriodYear.objects.order_by('Station'), label='Budżet roczny')
    month_period = forms.ModelChoiceField(queryset=PeriodMonth.objects.order_by('station'), label='Miesiąc')
    index = forms.FloatField(label='Index dopasowania')

class CalculateForm(forms.Form):
    package = forms.ModelChoiceField(queryset=Package.objects.order_by('station'), label='Pakiet')
    year_period = forms.ModelChoiceField(queryset=PeriodYear.objects.order_by('Station'), label='Budżet roczny')
    month_period = forms.ModelChoiceField(queryset=PeriodMonth.objects.order_by('station'), label='Miesiąc')
    index = forms.FloatField(label='Index dopasowania')

class DeleteStationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'