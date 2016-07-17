from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from data_obfuscator.modelupdate import process_file
from testobfuscator.models import MyModel
from django.db import models
from datetime import datetime, date
import random

class Command(BaseCommand):
    help = "Obfuscate the date field in model data's"

    option_list = BaseCommand.option_list + (
        make_option(
            "-m",
            "--model",
            dest = "model_name",
            help = "model name",
            metavar = "SLUG"
        ),
    )


    def handle(self, *args, **options):
        model_name = MyModel
        # for model_list in models.get_models(include_auto_created=False):
        #     print model_list
        for fields in model_name._meta.fields:
            field_name = fields.name

            if str(model_name._meta.get_field(field_name).get_internal_type) == \
                '<bound method DateField.get_internal_type of <django.db.models.fields.DateField: date>>':
                if model_name.objects.all().exists():
                    for items in model_name.objects.all():

                        current_year = date.today().year
                        rand_month = datetime.now().month
                        month = random.randint(rand_month -1, rand_month)
                        day = random.randint(30 - datetime.now().day, datetime.now().day)
                        birth_date = datetime(current_year, month, day)
                        items.date = birth_date.date()
                        items.save()
                        print model_name._meta.get_field(field_name)
                        print "birth date", birth_date
            else:
                pass