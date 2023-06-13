import requests
from django.core.management.base import BaseCommand
from teatimeapi.models import TeaListing, TeaDetails


class Command(BaseCommand):
    help = 'Populate data from external API'

    def tea(self, *args, **options):
        # Write your logic to fetch data from the external API
        response = requests.get('https://boonakitea.cyclic.app/api/all')
        data = response.json()

        # Write your logic to save the data to the existing model
        for i in data:
            if "image" not in i:
                tea = TeaListing(
                    name=i["name"],
                )
                tea.save()
            else:
                tea = TeaListing(
                    name=i["name"],
                    image=i["image"],
                )
                tea.save()

    def handle(self, *args, **options):
        # Write your logic to fetch data from the external API
        response = requests.get('https://boonakitea.cyclic.app/api/all')
        data = response.json()

        # Write your logic to save the data to the existing model
        for i in data:
            if "image" not in i:
                tea = TeaDetails(
                    name=i["name"],
                    image='',
                    origin=i["origin"],
                    tea_type=i["type"].capitalize(),
                    caffeine=i["caffeine"],
                    description=i["description"],
                    color=i["colorDescription"],
                    taste=i["tasteDescription"],
                )
                tea.save()
            elif "description" not in i:
                tea = TeaDetails(
                    name=i["name"],
                    image=i["image"],
                    origin=i["origin"],
                    tea_type=i["type"].capitalize(),
                    caffeine=i["caffeine"],
                    description="",
                    color=i["colorDescription"],
                    taste=i["tasteDescription"],
                )
                tea.save()

            else:
                tea = TeaDetails(
                    name=i["name"],
                    image=i["image"],
                    origin=i["origin"],
                    tea_type=i["type"].capitalize(),
                    caffeine=i["caffeine"],
                    description=i["description"],
                    color=i["colorDescription"],
                    taste=i["tasteDescription"],
                )
                tea.save()
