from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WorkerForm, EnquiryForm
from .models import Worker

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def worker_register(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_register')
    else:
        form = WorkerForm()
    return render(request, 'worker_register.html', {'form': form})

def customer_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_enquiry')
    else:
        form = EnquiryForm()
    return render(request, 'customer_enquiry.html', {'form': form})

def worker_list(request):
    workers = Worker.objects.all().order_by('-created_at')
    return render(request, 'worker_list.html', {'workers': workers})

def robots_txt(request):
    content = "User-agent: *\nAllow: /\n\nSitemap: http://127.0.0.1:8000/sitemap.xml\n"
    return HttpResponse(content, content_type="text/plain")

def sitemap_xml(request):
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>http://127.0.0.1:8000/</loc></url>
    <url><loc>http://127.0.0.1:8000/about/</loc></url>
    <url><loc>http://127.0.0.1:8000/faq/</loc></url>
    <url><loc>http://127.0.0.1:8000/worker-register/</loc></url>
    <url><loc>http://127.0.0.1:8000/customer-enquiry/</loc></url>
    <url><loc>http://127.0.0.1:8000/workers/</loc></url>
</urlset>"""
    return HttpResponse(content, content_type="application/xml")
