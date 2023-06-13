import requests
from django.core.management.base import BaseCommand
from teatimeapi.models import TeaType, TeaDetails


class Command(BaseCommand):
    help = 'Give Foreign Key to Tea Type in Tea Details'

    def handle(self, *args, **options):

        for i in TeaDetails.objects.all():
            for j in TeaType.objects.all():
                if i.tea_type == j.tea_type:
                    i.tea_type_num = j.id
