from django.shortcuts import render
from .lookup import perform_lookup
from django.http import JsonResponse


def search_view(request):
    q_params = request.GET
    q = q_params.get('q')
    context = {}

    if q is not None:
        results = perform_lookup(q, internal_sort=True)
        context['results'] = results
        context['query'] = q

    return render(request, 'search.html', context)
