from django.core.management.base import BaseCommand
from excel.models import Station, TVN_thematic_packages, TVP_thematic_packages, TVP_TOP4_package, Polsat_thematic_packages, Polsat_TOP4_packages

class Command(BaseCommand):
    help = 'dupa na kiju'


    def create_station(self, *args, **options):
        default_items = Station.def_items_station
        for krotka in default_items:
            Station.objects.create(name=krotka[1])

    def create_package_TVN(self, *args, **options):
        default_items = TVN_thematic_packages.def_items_TVN
        for krotka in default_items:
            TVN_thematic_packages.objects.create(name=krotka[1])

    def create_package_TVP(self, *args, **options):
        default_items = TVP_thematic_packages.def_items_TVP
        for krotka in default_items:
            TVP_thematic_packages.objects.create(name=krotka[1])

    def create_package_TVP_top4(self, *args, **options):
        default_items = TVP_TOP4_package.def_items_TVP_top4
        for krotka in default_items:
            TVP_TOP4_package.objects.create(name=krotka[1])

    def create_package_Polsat(self, *args, **options):
        default_items = Polsat_thematic_packages.def_items_Polsat
        for krotka in default_items:
            Polsat_thematic_packages.objects.create(name=krotka[1])

    def create_package_Polsat_top4(self, *args, **options):
        default_items = Polsat_TOP4_packages.def_items_Polsat_top4
        for krotka in default_items:
            Polsat_TOP4_packages.objects.create(name=krotka[1])
