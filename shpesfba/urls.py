from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/?$', RedirectView.as_view(url='/jobs/job-listings', permanent=False), name='jobs'),
    url(r'^jobs/job-listings?$', views.job_listings, name='jobs.job-listings'),
    url(r'^jobs/(?P<job_id>[0-9]+)/?$', views.job_detail, name='jobs.job-detail'),
    url(r'^jobs/add-job/?$', views.add_job, name='jobs.add-job'),
    url(r'^membership/?$', views.membership, name='membership'),
    url(r'^contact/?$', views.contact, name='contact'),
    url(r'^gallery/?$', views.gallery, name='gallery'),
    url(r'^upload-gallery-images/?$', views.upload_gallery_images, name='upload-gallery-images'),

    url(r'^about/?$', RedirectView.as_view(url='/about/shpesfba/', permanent=False), name='about'),
    url(r'^about/shpesfba/?$', TemplateView.as_view(template_name='shpesfba/about.shpesfba.html'), name='about.shpesfba'),
    url(r'^about/executive-board/?$', views.executive_board, name='about.executive-board'),
    url(r'^about/awards/?$', TemplateView.as_view(template_name='shpesfba/about.awards.html'), name='about.awards'),
    url(r'^about/chapter-history/?$', TemplateView.as_view(template_name='shpesfba/about.chapter.html'),
        name='about.chapter'),
    url(r'^about/SHPE/?$', TemplateView.as_view(template_name='shpesfba/about.shpe.html'), name='about.shpe'),
    url(r'^about/bylaws/?$', TemplateView.as_view(template_name='shpesfba/about.bylaws.html'), name='about.bylaws'),
    url(r'^calendar/?$', TemplateView.as_view(template_name='shpesfba/calendar.html'), name='calendar'),
    url(r'^about/past-events/?$', views.past_events, name='about.past-events'),

    url(r'latino-engineering-day/?$', TemplateView.as_view(template_name='shpesfba/latino-engineering-day.html'), name='latino-engineering-day'),

    url(r'^mentorshpe/?$', TemplateView.as_view(template_name='shpesfba/mentorshpe.html'), name='mentorshpe'),

    url(r'^contact.mailing-list/?$', TemplateView.as_view(template_name='shpesfba/contact.mailing-list.html'), name='contact.mailing-list'),
]

## debug stuff to serve static media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

