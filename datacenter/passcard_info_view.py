from django.utils.timezone import localtime
from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit


def get_visits_by_passcode(passcode):
    return Visit.objects.filter(passcard__passcode=passcode)


def get_duration(visit):
    duration = localtime() - localtime(visit.entered_at)
    return format_duration(duration)


def format_duration(duration):
    return f"{duration.seconds // 3600}:{duration.seconds % 60}"


def is_visit_long(visit, minutes=60):
    duration_in_minutes = int(get_duration(visit).strip(':')[0])
    return duration_in_minutes > minutes


def passcard_info_view(request, passcode):
    # Программируем здесь
    this_passcard_visits = []
    for visit in get_visits_by_passcode(passcode):
        this_passcard_visits.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': get_duration(visit),
                'is_strange': is_visit_long(visit),
            }
        )

    context = {
        'passcard': Passcard.objects.get(passcode=passcode),
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
