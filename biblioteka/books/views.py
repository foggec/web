from django.shortcuts import render
from .models import artic
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.staticfiles.storage import staticfiles_storage
import random
from django.core.paginator import Paginator
from django.db.models import Q
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from users import views as users_views

def book_home(request):
    books = artic.objects.order_by('title')
    return render(request, 'books/book_home.html', {'books': books})

class bookDetail(DetailView):
    model = artic
    template_name = 'books/detailss.html'
    context_object_name = 'article'

@login_required
def game_detail(request, book_id):
    articz = get_object_or_404(artic, book_id=book_id)
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Updating backlog section
        b_section = request.POST.get('b_section')

        # Убираем книгу из других категорий, если она там была
        for category in ['want_to_read', 'reading', 'reaed', 'completed']:
            if category != b_section and articz in getattr(user_profile, category).all():
                getattr(user_profile, category).remove(articz)

        # Добавляем книгу в выбранную категорию
        if b_section in ['want_to_read', 'reading', 'reaed', 'completed']:
            getattr(user_profile, b_section).add(articz)

    context = {
        'game': articz
    }
    return render(request, 'books/book_detail.html', context)
