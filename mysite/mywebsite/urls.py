from django.conf.urls import patterns, include, url
from django.contrib import admin
from mywebsite import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'index.html', views.index, name='index'),
    url(r'about.html', views.about, name='about'),
    url(r'services.html', views.services, name='services'),
    url(r'contact.html', views.contact, name='contact'),
    url(r'portfolio-1-col.html', views.portfolio_first, name='portfolio-first'),
    url(r'portfolio-2-col.html', views.portfolio_first, name='portfolio-second'),
    url(r'portfolio-3-col.html', views.portfolio_first, name='portfolio-third'),
    url(r'portfolio-4-col.html', views.portfolio_first, name='portfolio-fourth'),
    url(r'faq.html', views.faq, name='faq'),
    url(r'pricing.html', views.pricing, name='pricing'),
)
