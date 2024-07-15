import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from suivi.models import Planitems, Plans

class Command(BaseCommand):
    help = 'Migrate data from CSV file to Planitems model'

    def handle(self, *args, **options):
        csv_file_path = settings.BASE_DIR / 'datas' / 'planitems.csv'

        with open(csv_file_path, 'r', encoding='latin1') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row_index, row in enumerate(csv_reader, start=1):
                plan_id_str = row.get("plan_id")
                if not plan_id_str or not plan_id_str.isdigit():
                    self.stderr.write(self.style.ERROR(f'Invalid or missing plan_id in row {row_index}. Skipping entry.'))
                    continue

                plan_id = int(plan_id_str)
                try:
                    plan = Plans.objects.get(id=plan_id)
                except Plans.DoesNotExist:
                    self.stderr.write(self.style.ERROR(f'Plan ID {plan_id} does not exist. Skipping entry.'))
                    continue

                agent_id_str = row.get('agent_id', '')
                if agent_id_str:
                    try:
                        agent_id = int(agent_id_str)
                        agent = User.objects.get(id=agent_id)
                    except (ValueError, User.DoesNotExist):
                        self.stderr.write(self.style.ERROR(f'Invalid or missing agent_id for row {row_index}. Skipping entry.'))
                        continue
                else:
                    agent = None

                planitem_data = {
                    'num_ordre': row.get('num_ordre', ''),
                    'budget': row.get('budget', ''),
                    'typcredit': row.get('typcredit', ''),
                    'immobilisation': row.get('immobilisation', ''),
                    'credit': row.get('credit', ''),
                    'centre_cout': row.get('centre_cout', ''),
                    'projet': row.get('projet', ''),
                    'localisation': row.get('localisation', ''),
                    'montant_estime': row.get('montant_estime', ''),
                    'composante': row.get('composante', ''),
                    'montant_dispo': row.get('montant_dispo', ''),
                    'designation': row.get('designation', ''),
                    'type': row.get('type', ''),
                    'mode': row.get('mode', ''),
                    'nbr_lot': row.get('nbr_lot', ''),
                    'agent_id': agent,
                    'date_tech': row.get('date_tech', ''),
                    'date_tech_reel': row.get('date_tech_reel', ''),
                }

                # Use update_or_create method to create planitems line in you dabase
                planitem, created = Planitems.objects.update_or_create(**planitem_data)
                planitem.plan_id = plan
                planitem.agent_id = agent
                planitem.save()

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Planitem {planitem.num_ordre} created for Plan ID {plan_id}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Planitem {planitem.num_ordre} updated for Plan ID {plan_id}'))
            
            #Fin d'importation 
            self.stdout.write(self.style.SUCCESS(f'.................Fin d\'importation.........'))
