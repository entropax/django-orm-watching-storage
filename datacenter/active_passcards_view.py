from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    all_passcards = Passcard.objects.all()
    all_active = all_passcards.filter(is_active=True)
    context = {
        'active_passcards': all_active,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
