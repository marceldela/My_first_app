from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from excel import models

from excel.forms import CreateStationForm, CreatePackageForm, CreatePeriodYearForm, CreatePeriodMonthForm, \
    CreateIndexPackageForm, CalculateForm, CalculateFormMax, CalculateFormMin, DeleteStationForm

from excel.models import Station, Package, PeriodYear, PeriodMonth, IndexPackage


class StationView(View):

    def get(self, request):
        stations = Station.objects.all()
        return render(request, "station.html", {'stations': stations})

class CreateStationView(View):

    def get(self, request):
        form = CreateStationForm()
        return render(request, 'CreateStation.html', {'form':form})

    def post(self, request):
        form = CreateStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/create_package/")


class PackageView(View):

    def get(self, request, id_station):
        packages = Package.objects.filter(station_id=id_station)
        return render(request, 'package.html', {'packages': packages})

class CreatePackageView(View):

    def get(self, request):
        form = CreatePackageForm()
        return render(request, 'CreatePackage.html', {'form':form})
    def post(self, request):
        form = CreatePackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/create_periodyear/")

class PeriodYearView(View):

    def get(self, request, id_station):
        periods = PeriodYear.objects.filter(Station__id=id_station)
        return render(request, 'period_year.html', {'periods': periods})

class CreatePeriodYearView(View):

    def get(self, request):
        form = CreatePeriodYearForm()
        return render(request, 'CreatePeriodYear.html', {'form':form})

    def post(self, request):
        form = CreatePeriodYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create_periodmonth/')

class PeriodMonthView(View):

    def get(self, request, id_station):
        periods = PeriodMonth.objects.filter(station__id=id_station)
        return render(request, 'period_month.html', {'periods': periods})



class CreatePeriodMonthView(View):

    def get(self, request):
        form = CreatePeriodMonthForm()
        return render(request, 'CreatePeriodMonth.html', {'form':form})

    def post(self, request):
        form = CreatePeriodMonthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create_index/')

class IndexPackageView(View):

    def get(self, request, id_package):
        indexes = IndexPackage.objects.filter(package__id=id_package)
        return render(request, 'index_package.html', {'indexes':indexes})

class CreateIndexPackageView(View):
    def get(self, request):
        form = CreateIndexPackageForm()
        return render(request, 'CreateIndexPackage.html', {'form':form})

    def post(self, request):
        form = CreateIndexPackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calculate/')

class CalculateMin(View):
    def get(self, request):
        form = CalculateFormMin()
        return render(request, 'calculatemin.html', {'form':form})

    def post(self,request):
        form = CalculateFormMin(request.POST)
        if form.is_valid():
            package = form.cleaned_data['package']
            per_month = form.cleaned_data['month_period']
            period_year = form.cleaned_data['year_period']
            ind_dopasowania = form.cleaned_data['index']
            min = period_year.CPP_min
            ip = IndexPackage.objects.get(pakiet=package, period_year=period_year)
            val = min / ind_dopasowania * per_month.index_month * ip.index
            return HttpResponse(val)

class CalculateMax(View):
    def get(self, request):
        form = CalculateFormMax()
        return render(request, 'calculatemax.html', {'form':form})

    def post(self, request):
        form = CalculateFormMax(request.POST)
        if form.is_valid():
            package = form.cleaned_data['package']
            per_month = form.cleaned_data['month_period']
            period_year = form.cleaned_data['year_period']
            ind_dopasowania = form.cleaned_data['index']
            max = period_year.CPP_max
            ip = IndexPackage.objects.get(pakiet=package, period_year=period_year)
            val = max / ind_dopasowania * per_month.index_month * ip.index
            return HttpResponse(val)

class Calculate(View):
    def get(self, request):
        form = CalculateForm()
        return render(request, 'calculate.html', {'form': form})

    def post(self, request):
        form = CalculateForm(request.POST)
        if form.is_valid():
            package = form.cleaned_data['package']
            per_month = form.cleaned_data['month_period']
            period_year = form.cleaned_data['year_period']
            ind_dopasowania = form.cleaned_data['index']
            cpp = period_year.CPP
            ip = IndexPackage.objects.get(pakiet=package, period_year=period_year)
            val = cpp / ind_dopasowania * per_month.index_month * ip.index
            return HttpResponse(val)

class StationDelete(View):
    def get(self, request, station_id):
        to_delete = models.Station.objects.get(id=station_id)
        to_delete.delete()
        all_station = models.Station.objects.all()
        return render(request, 'station.html', {'stations':all_station})

class PackageDelete(View):
    def get(self, request, package_id):
        to_delete = models.Package.objects.get(id=package_id)
        to_delete.delete()
        all_packages = models.Package.objects.all()
        return render(request, 'package.html', {'packages':all_packages})

class PackageViewAll(View):

    def get(self, request):
        packages_all = models.Package.objects.all()
        return render(request, 'package.html', {'packages': packages_all})


class YearDelete(View):
    def get(self, request, year_id):
        to_delete = models.PeriodYear.objects.get(id=year_id)
        to_delete.delete()
        all_years = models.PeriodYear.objects.all()
        return render(request, 'period_year.html', {'periods': all_years})


class YearViewAll(View):

    def get(self, request):
        all_years = models.PeriodYear.objects.all()
        return render(request, 'period_year.html', {'periods': all_years})

class MonthViewAll(View):

    def get(self, request):
        all_months = models.PeriodMonth.objects.all()
        return render(request, 'period_month.html', {'periods': all_months})

class MonthDelete(View):
    def get(self, request, month_id):
        to_delete = models.PeriodMonth.objects.get(id=month_id)
        to_delete.delete()
        all_months = models.PeriodMonth.objects.all()
        return render(request, 'period_month.html', {'periods': all_months})

class IndexViewAll(View):

    def get(self, request):
        all_indexes = models.IndexPackage.objects.all()
        return render(request, 'index_package.html', {'indexes': all_indexes})

class IndexDelete(View):
    def get(self, request, index_id):
        to_delete = models.IndexPackage.objects.get(id=index_id)
        to_delete.delete()
        all_indexes = models.IndexPackage.objects.all()
        return render(request, 'index_package.html', {'indexes': all_indexes})