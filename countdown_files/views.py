from django.shortcuts import render, redirect
import datetime
import time
# from pytz import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calculate_time_remaining(target_date, current_time):
    time_remaining = target_date - current_time
    return time_remaining.total_seconds()

def countdown(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        date = request.POST.get('date')
        time = request.POST.get('time')
        target_date = datetime.datetime.strptime(date + ' ' + time, "%Y-%m-%d %H:%M")
        formatted_date = target_date.strftime("%B %d, %Y")

        while True:
            # Get the current date and time
            current_time = datetime.datetime.now()

            # Calculate the time remaining until the target date and time
            time_remaining = calculate_time_remaining(target_date, current_time)
            
            break

        return render(request, 'countdown.html', {'event': event, 'time_remaining': time_remaining, 'formatted_date': formatted_date})
    else:
        return redirect('home')
