"""Media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from excel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CreateStationView.as_view(), name='create_station'),
    path('station/', views.StationView.as_view(), name='station'),
    path('package/<int:id_station>/', views.PackageView.as_view(), name='package'),
    path('create_package/', views.CreatePackageView.as_view(), name='create_package'),
    path('period_year/<int:id_station>/', views.PeriodYearView.as_view(), name='period_year'),
    path('create_periodyear/', views.CreatePeriodYearView.as_view(), name='create_periodyear'),
    path('period_month/<int:id_station>/', views.PeriodMonthView.as_view(), name='period_month'),
    path('create_periodmonth/', views.CreatePeriodMonthView.as_view(), name='create_periodmonth'),
    #path('index/<int:id_package>/', views.IndexPackageView.as_view(), name='index'),
    path('create_index/', views.CreateIndexPackageView.as_view(), name='create_index'),
    path('calculate_min/', views.CalculateMin.as_view(), name='cpp_min'),
    path('calculate_max/', views.CalculateMax.as_view(), name='cpp_max'),
    path('calculate/', views.Calculate.as_view(), name='cpp'),
    path('delete_station/<int:station_id>/', views.StationDelete.as_view(), name='delete_station'),
    path('delete_package/<int:package_id>/', views.PackageDelete.as_view(), name='delete_package'),
    path('package/', views.PackageViewAll.as_view(), name='packages_all'),
    path('period_year/', views.YearViewAll.as_view(), name='years_all'),
    path('period_month/', views.MonthViewAll.as_view(), name='months_all'),
    path('indexes/', views.IndexViewAll.as_view(), name='indexes_all'),
    path('delete_year/<int:year_id>/', views.YearDelete.as_view(), name='delete_year'),
    path('delete_index/<int:index_id>/', views.IndexDelete.as_view(), name='delete_index'),
    path('delete_month/<int:month_id>/', views.MonthDelete.as_view(), name='delete_month'),

]
