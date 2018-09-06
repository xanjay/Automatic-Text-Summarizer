import os
from pprint import pprint
from .models import Document
from django.shortcuts import render
from django.http import HttpResponse
from .Scraping.Scraping import bbc_scraping, cnn_scraping, nagarik_scraping
from .forms import DocumentForm
from django.conf import settings
from .pdf_summarizer import summarize_pdf


def index(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        news = []
        if source == "'BBC'":
            news = bbc_scraping()
        elif source == "'CNN'":
            news = cnn_scraping()
        elif source == "'Nagarik'":
            news = nagarik_scraping()

        context = {'source': source, 'news': news}
        return render(request, 'news/news.html', context)


def file_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            summary_p = form.cleaned_data['summary_p']
            file_name = form.cleaned_data['document'].name
            file_name = file_name.replace(' ', '_')
            outputfile = file_name[:-4]
            out_file_name = outputfile+'.txt'

            form.save()

            media_root = getattr(settings, 'MEDIA_ROOT', None)
            file_location = os.path.join(media_root, file_name)

            summary = summarize_pdf(file_location, summary_p)
            response = HttpResponse(summary, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(out_file_name)

            os.remove(os.path.join(media_root, file_location))

            Document.objects.all().delete()

            return response
    else:
        form = DocumentForm()
    return render(request, 'news/file_form.html', {
        'form': form
    })
