from django.core.management.base import BaseCommand
from mysite.models import People

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print "Hello, World!"
        print People.objects.count()
