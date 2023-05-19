from django.contrib import messages
from django.shortcuts import redirect, render

from lineup.models import Performance


def add_performances(request):
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith('act-'):
                index = key.split('-')[1]
                act = request.POST.get(f'act-{index}')
                start_time = request.POST.get(f'start_time-{index}')
                end_time = request.POST.get(f'end_time-{index}')
                contact_name = request.POST.get(f'contact_name-{index}')

                # Validate and save data here
                # performance = Performance(
                #     act=act,
                #     start_time=start_time,
                #     end_time=end_time,
                #     contact_name=contact_name
                # )
                # performance.save()
        messages.success(request, "Performances have been added successfully!")
        return redirect('add_performances')
    else:
        return render(request, 'producer/add_performances.html')