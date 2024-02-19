from django.shortcuts import render
from django.http import JsonResponse
from .models import Booking, Table, Restaurant
# Create your views here.


def make_booking(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        num_guests = int(request.POST.get('num_guests'))
        
         # Validate input
        if not date or not time or num_guests <= 0:
            return JsonResponse({'message': 'Invalid input. Please provide valid date, time, and number of guests.'}, status=400)

        # Check availability
        if is_table_available(date, time, num_guests):
            # Create a new booking
            booking = Booking.objects.create(date=date, time=time, num_guests=num_guests)
            # Update table availability
            update_table_availability(date, time, num_guests)
            return JsonResponse({'message': 'Booking successful!'})
        else:
            return JsonResponse({'message': 'Sorry, no tables available at this time.'}, status=400)
    return render(request, 'booking/booking_form.html')

def is_table_available(date, time, num_guests):
    tables = Table.objects.filter(date=date, time=time, is_available=True)
    for table in tables:
        if table.capacity >= num_guests:
            return True
    return False

def update_table_availability(date, time, num_guests):
    tables = Table.objects.filter(date=date, time=time, is_available=True)
    for table in tables:
        if table.capacity >= num_guests:
            table.is_available = False
            table.save()
            return

def my_view(request):
    total_tables = Restaurant.objects.first().total_tables