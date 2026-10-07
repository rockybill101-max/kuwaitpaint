from django.contrib import admin
from django.urls import path
from workers import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('worker-register/', views.worker_register, name='worker_register'),
    path('customer-enquiry/', views.customer_enquiry, name='customer_enquiry'),
    path('workers/', views.worker_list, name='worker_list'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
]
