from django.conf.urls import url
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

    url(r'^about/?$', RedirectView.as_view(url='/about/executive-board', permanent=False), name='about'),
    url(r'^about/executive-board/?$', views.executive_board, name='about.executive-board'),
    url(r'^about/chapter-history/?$', TemplateView.as_view(template_name='shpesfba/about.chapter.html'),
        name='about.chapter'),
    url(r'^about/SHPE/?$', TemplateView.as_view(template_name='shpesfba/about.shpe.html'), name='about.shpe'),
    url(r'^about/bylaws/?$', TemplateView.as_view(template_name='shpesfba/about.bylaws.html'), name='about.bylaws'),
    url(r'^about/past-events/?$', views.past_events, name='about.past-events'),
]
