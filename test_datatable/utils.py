from django.core.paginator import Paginator 
from test_site.settings import NUMBER_Of_POSTS


def get_page_context(queryset, request):
    paginator = Paginator(queryset, NUMBER_Of_POSTS)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=int(page_number),
                                                 on_each_side=2,
                                                 on_ends=1)
    return { 
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
        'page_range': page_range,
    }
