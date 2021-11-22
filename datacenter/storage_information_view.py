from django.utils.timezone import localtime

from datacenter.models import Visit
from django.shortcuts import render


def get_visitors_in_vault():
    visitors_in_vault = Visit.objects.filter(leaved_at=None)
    return visitors_in_vault


def get_duration(visit):
    duration = localtime() - localtime(visit.entered_at)
    return format_duration(duration)


def format_duration(duration):
    return f"{duration.seconds // 3600}:{duration.seconds % 60}"


def format_date(date):
    return date.strftime('%d-%m-%Y, %H:%M')


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    for visitor in get_visitors_in_vault():
        visit_dict = {}
        visit_dict['who_entered'] = visitor.passcard.owner_name
        visit_dict['entered_at'] = format_date(localtime(visitor.entered_at))
        visit_dict['duration'] = get_duration(visitor)
        non_closed_visits.append(visit_dict)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
