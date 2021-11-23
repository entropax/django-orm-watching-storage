from django.utils.timezone import localtime

from datacenter.models import Visit
from django.shortcuts import render


def format_date(date):
    return date.strftime('%d-%m-%Y, %H:%M')


def storage_information_view(request):
    non_closed_visits = []
    for visitor in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard.owner_name,
                'entered_at': format_date(localtime(visitor.entered_at)),
                'duration': visitor.formated_duration(),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
