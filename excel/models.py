from django.db import models
from django.forms import ModelForm


class Station(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa stacji')

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa pakietu')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name='Stacja')

    def __str__(self):
        return self.name



class PeriodYear(models.Model):
    name = models.CharField(max_length=128, verbose_name='Budżet roczny')
    CPP_min = models.IntegerField(blank=True)
    CPP_max = models.IntegerField(blank=True)
    CPP = models.IntegerField(blank=True)
    Station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name='Stacja')


    def __str__(self):
        return f"{self.name} {self.Station}"


class PeriodMonth(models.Model):
    name = models.CharField(max_length=128, verbose_name='miesiąc')
    index_month = models.FloatField(null=False, verbose_name='Index miesiąca')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name='Stacja')

    def __str__(self):
        return f"{self.name} {self.station}"


class IndexPackage(models.Model):
    pakiet = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Pakiet')
    period_year = models.ForeignKey(PeriodYear, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Budżet roczny')
    index = models.FloatField(verbose_name='index pakietu')


    def __str__(self):
        return self.index

