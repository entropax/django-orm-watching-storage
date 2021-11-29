import datetime
from django.utils.timezone import localtime
from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit


def is_visit_long(visit, minutes=60) -> bool:
    duration = visit.get_duration()
    alarming_duration = datetime.timedelta(minutes=minutes)
    return duration > alarming_duration


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard__passcode=passcode):
        this_passcard_visits.append(
            {
                "entered_at": localtime(visit.entered_at),
                "duration": visit.get_duration(),
                "is_strange": is_visit_long(visit),
            }
        )
    context = {
        "passcard": Passcard.objects.get(passcode=passcode),
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, "passcard_info.html", context)
