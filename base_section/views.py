from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request, 'base_section/index.html', {
        'mainsection_active': 'active'
    })