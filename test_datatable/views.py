import datetime

from django.shortcuts import render
from .models import Modalities, Studies
# import names
import random
from datetime import timedelta
import uuid
from .utils import get_page_context
from django.db.models import Q


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_db(request):
    """
    База предоставляется уже предзаполненной, но в случае желания перехода
    на другую СУБД, можно раскомментировать код ниже и сгенерировать тестовые данные.
    """
    query = request.GET.get('q')
    sort = request.GET.get('s')
    params = ''
    params_sort = ''
    if query:
        studies = Studies.objects.filter(
                Q(patient_fio__icontains=query
                  ) | Q(study_uid__icontains=query
                        ) | Q(patient_birthdate__icontains=query
                              ) | Q(study_date__icontains=query
                                    ) | Q(study_modality__name=query)
            )
        params += f'&q={query}'
        params_sort += f'&q={query}'
        if sort:
            studies = studies.order_by(sort)
            params += f'&s={sort}'
    elif sort:
        studies = Studies.objects.all().order_by(sort)
        params += f'&s={sort}'
    else:
        studies = Studies.objects.all()
    context = get_page_context(studies, request)
    context['params'] = params
    context['params_sort'] = params_sort
    return render(request, 'test_datatable/init_db.html', context)
