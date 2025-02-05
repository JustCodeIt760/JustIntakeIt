from django.core.management.base import BaseCommand
from project_initiation.models import Route, Stop, Vehicle
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Creates sample stops for Atlanta airport terminals and parking lots'

    def handle(self, *args, **kwargs):
        # Create main route
        route, _ = Route.objects.get_or_create(
            name='ATL Terminal Route',
            description='Main route connecting all terminals and parking lots'
        )

        # Terminal stops
        terminals = [
            {
                'name': 'Domestic Terminal North',
                'lat': 33.6407,
                'lng': -84.4277,
                'seq': 1
            },
            {
                'name': 'Domestic Terminal South',
                'lat': 33.6397,
                'lng': -84.4277,
                'seq': 2
            },
            {
                'name': 'International Terminal',
                'lat': 33.6424,
                'lng': -84.4224,
                'seq': 3
            },
        ]

        # Parking lot stops
        parking_lots = [
            {
                'name': 'North Daily Parking',
                'lat': 33.6437,
                'lng': -84.4277,
                'seq': 4
            },
            {
                'name': 'South Daily Parking',
                'lat': 33.6367,
                'lng': -84.4277,
                'seq': 5
            },
            {
                'name': 'Economy Lot',
                'lat': 33.6457,
                'lng': -84.4307,
                'seq': 6
            },
        ]

        # Create all stops
        all_stops = terminals + parking_lots
        for stop_data in all_stops:
            stop, created = Stop.objects.get_or_create(
                name=stop_data['name'],
                route=route,
                defaults={
                    'latitude': stop_data['lat'],
                    'longitude': stop_data['lng'],
                    'sequence_number': stop_data['seq'],
                    'estimated_wait_time': 5
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created stop: {stop.name}'))

        # Create sample vehicles
        vehicle_ids = ['ATL001', 'ATL002', 'ATL003']
        current_time = timezone.now()

        for idx, vehicle_id in enumerate(vehicle_ids):
            # Calculate position based on route progress
            progress = (idx / len(vehicle_ids)) * len(all_stops)
            current_stop_idx = int(progress)
            next_stop_idx = (current_stop_idx + 1) % len(all_stops)

            current_stop = Stop.objects.get(sequence_number=current_stop_idx + 1)
            next_stop = Stop.objects.get(sequence_number=next_stop_idx + 1)

            # Create or update vehicle
            vehicle, created = Vehicle.objects.get_or_create(
                identifier=vehicle_id,
                defaults={
                    'route': route,
                    'current_latitude': current_stop.latitude,
                    'current_longitude': current_stop.longitude,
                    'is_active': True,
                    'next_stop': next_stop,
                    'estimated_arrival': current_time + timedelta(minutes=5 + (idx * 3))
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created vehicle: {vehicle.identifier}'))

        self.stdout.write(self.style.SUCCESS('Successfully created all stops and vehicles'))