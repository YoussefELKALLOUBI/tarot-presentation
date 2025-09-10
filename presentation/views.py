from django.shortcuts import render

def home(request):
    """Page d'accueil - Présentation générale du réseau TAROT"""
    context = {
        'page_title': 'Accueil - Réseau TAROT',
        'current_page': 'home'
    }
    return render(request, 'presentation/home.html', context)

def sites_overview(request):
    """Vue d'ensemble des 4 sites TAROT"""
    sites_data = [
        {
            'name': 'TAROT France',
            'location': 'Calern, France',
            'coordinates': '43.7489° N, 6.9239° E',
            'altitude': '1270m',
            'status': 'Opérationnel',
            'year_installed': '2006'
        },
        {
            'name': 'TAROT Chili',
            'location': 'La Silla, Chili',
            'coordinates': '29.2584° S, 70.7345° W',
            'altitude': '2400m',
            'status': 'Opérationnel',
            'year_installed': '2009'
        },
        {
            'name': 'TAROT Réunion',
            'location': 'Les Makes, Réunion',
            'coordinates': '21.2058° S, 55.3706° E',
            'altitude': '1000m',
            'status': 'Opérationnel',
            'year_installed': '2013'
        },
        {
            'name': 'TAROT Nouvelle-Calédonie',
            'location': 'Nouvelle-Calédonie',
            'coordinates': '22.2758° S, 166.4581° E',
            'altitude': '400m',
            'status': 'Récemment installé',
            'year_installed': '2024'
        }
    ]
    
    context = {
        'page_title': 'Sites TAROT dans le monde',
        'current_page': 'sites',
        'sites': sites_data
    }
    return render(request, 'presentation/sites.html', context)

def mission(request):
    """Page mission et objectifs"""
    context = {
        'page_title': 'Mission et Objectifs',
        'current_page': 'mission'
    }
    return render(request, 'presentation/mission.html', context)

def pyros_software(request):
    """Page sur le logiciel PyROS"""
    context = {
        'page_title': 'Logiciel PyROS',
        'current_page': 'pyros'
    }
    return render(request, 'presentation/pyros.html', context)

def contact(request):
    """Page contact"""
    context = {
        'page_title': 'Contact',
        'current_page': 'contact'
    }
    return render(request, 'presentation/contact.html', context)

def quiz(request):
    context = {
        'page_title': 'Quiz Spatial TAROT',
        'current_page': 'quiz'
    }
    return render(request, 'presentation/quiz.html', context)


    
def tarot_map_view(request):
    context = {
        'page_title': 'Réseau TAROT - Couverture Mondiale',
        'current_page': 'map',
        'sites': [
            {
                'name': 'TAROT France',
                'flag': '🇫🇷',
                'location': 'Calern, France',
                'coordinates': '43.7489° N, 6.9239° E',
                'altitude': '1270m',
                'status': 'Opérationnel',
                'timezone': 1,
                'position': {'top': '25%', 'left': '48%'}
            },
            {
                'name': 'TAROT Chili',
                'flag': '🇨🇱',
                'location': 'La Silla, Chili',
                'coordinates': '29.2584° S, 70.7345° W',
                'altitude': '2400m',
                'status': 'Opérationnel',
                'timezone': -3,
                'position': {'top': '45%', 'left': '25%'}
            },
            {
                'name': 'TAROT Réunion',
                'flag': '🇷🇪',
                'location': 'Les Makes, Réunion',
                'coordinates': '21.2058° S, 55.3706° E',
                'altitude': '1000m',
                'status': 'Opérationnel',
                'timezone': 4,
                'position': {'top': '55%', 'left': '55%'}
            },
            {
                'name': 'TAROT Nouvelle-Calédonie',
                'flag': '🇳🇨',
                'location': 'Nouvelle-Calédonie',
                'coordinates': '22.2758° S, 166.4581° E',
                'altitude': '400m',
                'status': 'Récent',
                'timezone': 11,
                'position': {'top': '50%', 'left': '85%'}
            }
        ]
    }
    return render(request, 'presentation/map.html', context)


def custom_404_view(request, exception):
    """Vue personnalisée pour les erreurs 404"""
    return render(request, 'presentation/404.html', status=404)
