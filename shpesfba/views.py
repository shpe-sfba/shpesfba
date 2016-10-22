import datetime
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from shpesfba.models import Officer, Event, JobPosting, Membership, MessageForm, MessageType, JobPostingForm, Gallery


def index(request):
    dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
    events = Event.objects.filter(date__gte=timezone.make_aware(dt)).order_by('date')
    context = {
        'events': events
    }
    return render(request, 'shpesfba/home.html', context)


def executive_board(request):
    officers_list = Officer.objects.order_by('role__list_position')
    context = {
        'officers': officers_list
    }
    return render(request, 'shpesfba/officers.html', context)


def job_listings(request):
    dt = datetime.datetime.now().replace(hour=0, minute=0, second=0)
    jobs = JobPosting.objects.filter(approved=True, expiration_date__gte=timezone.make_aware(dt)).order_by('-expiration_date')
    context = {
        'jobs': jobs
    }
    return render(request, 'shpesfba/jobs.job_listings.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, pk=job_id)
    return render(request, 'shpesfba/jobs.job_detail.html', {'job': job})


def add_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job submitted successfully. Please give us a few days to review it for posting.', extra_tags='alert-success')
            return redirect('jobs.add-job')
    else:
        form = JobPostingForm()

    return render(request, 'shpesfba/jobs.add_job.html', {'form': form})


def membership(request):
    memberships = Membership.objects.all()
    context = {
        'memberships': memberships
    }
    return render(request, 'shpesfba/memberships.html', context)


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "From: {} <{}>\r\nType: {} ({})\r\n\r\n{}".format(form.cleaned_data['name'], form.cleaned_data['email'],
                                                               form.cleaned_data['message_type'].title,
                                                               form.cleaned_data['message_type'].responsible_officer_role.email,
                                                               form.cleaned_data['message'])

            send_notice('Message from SHPE SF BA Site', msg)
            messages.success(request, 'Message sent successfully. We\'ll reply as soon as possible.', extra_tags='alert-success')
            return redirect('contact')

    else:

        if request.GET.get('action', None) == 'mailing_list':
            message_type = MessageType.objects.get(title='Join our Mailing List')
            form = MessageForm(initial = {'message_type':message_type.pk})
        else:
            form = MessageForm()


    return render(request, 'shpesfba/contact.html', {'form': form})


def past_events(request):
    events_list = Event.objects.all().order_by('-date')
    paginator = Paginator(events_list, 10)

    page = request.GET.get('page')

    try:
        events = paginator.page(page)
        page = int(page)
    except PageNotAnInteger:
        events = paginator.page(1)
        page = 1
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
        page = paginator.num_pages

    context = {
        'events': events,
        'pagesBefore': range(1, page),
        'pagesAfter': range(page + 1, paginator.num_pages + 1)
    }
    return render(request, 'shpesfba/about.past-events.html', context)


def send_notice(subject, msg):
    msg_from = 'webmaster@shpesfba.org'
    to = ['webmaster@shpesfba.org']

    send_mail(
        subject,
        msg,
        msg_from,
        to,
        fail_silently=True,
    )


def gallery(request):
    galleries = Gallery.objects.all().order_by('-date_created')
    context = {
        'galleries': galleries
    }
    return render(request, 'shpesfba/gallery.html', context)