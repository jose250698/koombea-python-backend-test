from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.utils.html import strip_tags
from .models import Page, Link


@shared_task
def scrape_page(page_id):
    page = Page.objects.get(id=page_id)
    try:
        response = requests.get(page.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page.title = soup.title.string if soup.title else 'No Title'
        links = soup.find_all('a', href=True)
        page.total_links = len(links)
        for link in links:
            link_text = strip_tags(str(link))
            Link.objects.create(page=page, url=link['href'], name=link_text)
    except Exception as e:
        page.title = f'Error: {str(e)}'
    page.is_processing = False
    page.save()
