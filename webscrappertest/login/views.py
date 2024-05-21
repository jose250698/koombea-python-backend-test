from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Page, Link
from .tasks import scrape_page
from .forms import PageForm


@login_required
def home(request):
    pages = Page.objects.all()
    return render(request, 'home.html', {'pages': pages})

def auth_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    else:
        form = UserCreationForm()
    return render(
        request,
        'registration/signup.html',
        {"form": form}
    )


@login_required
def add_url(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.user = request.user
            page.save()
            scrape_page(page.id)
            return redirect('login:home')
    else:
        form = PageForm()
    return render(request, 'add_url.html', {'form': form})


@login_required
def page_detail(request, page_id):
    page = Page.objects.get(id=page_id, user=request.user)
    links = Link.objects.filter(page=page)
    return render(request, 'page_detail.html', {'page': page, 'links': links})
