# finance_app/management/commands/import_csv_data.py

import csv
from django.core.management.base import BaseCommand
from finance_app.models import FinanceRate

class Command(BaseCommand):
    help = 'Import CSV data into FinanceRate model'

    def handle(self, *args, **kwargs):
        csv_file = 'data.csv'  # Path to your CSV file

        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                age = int(row[0])
                rates = [float(rate) for rate in row[1:]]

                # Create or update FinanceRate object
                finance_rate, created = FinanceRate.objects.update_or_create(
                    age=age,
                    defaults={
                        'rate_3_0': rates[0],
                        'rate_3_125': rates[1],
                        'rate_3_25': rates[2],
                        'rate_3_375': rates[3],
                        'rate_3_5': rates[4],
                        'rate_3_625': rates[5],
                        'rate_3_75': rates[6],
                        'rate_3_875': rates[7],
                        'rate_4_0': rates[8],
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created FinanceRate object for age {age}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated FinanceRate object for age {age}'))
