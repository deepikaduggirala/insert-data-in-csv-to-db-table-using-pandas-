from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from accounts.models import *
import pandas as pd


class Command(BaseCommand):
    help = 'Insert PageAccess Label names'
    def handle(self, *args, **options):
    	file_path = settings.MEDIA_ROOT + "pageaccess"
        dir_list = [name for name in os.listdir(file_path)]
        input_file_list = set([file for file in os.listdir(file_path) if file.endswith(".csv")])
        for each_file in list(input_file_list):
        	file_name = file_path+'/'+each_file
        	print file_name
        	df = pd.read_csv(file_name)
        	for each_row in df.index:
	        	try:
		        	pa_obj=PageAccess.objects.get(page_name=df['page_name'][each_row])
		        	pa_obj.label_name = df['label_name'][each_row]
		        	pa_obj.save()

		       	except PageAccess.DoesNotExist as e:
		       		kwargs={
		       		'page_name':df['page_name'][each_row],
		       		'label_name':df['label_name'][each_row]
		       		}
		       		
		       		pa_obj=PageAccess.objects.create(**kwargs)
		       		print pa_obj,"helo"
		       		pa_obj.save()

        	