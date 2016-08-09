import datetime

from django.shortcuts import render, get_object_or_404

from shpesfba.models import Officer, Event, JobPosting, Membership, MessageForm, JobPostingForm


def index(request):
    events = Event.objects.filter(date__gte=datetime.datetime.today()).order_by('date')
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
    jobs = JobPosting.objects.all()
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
            form = JobPostingForm()
            return render(request, 'shpesfba/jobs.add_job.html', {'form': form, 'success': True})
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
            form = MessageForm()
            return render(request, 'shpesfba/contact.html', {'form': form, 'success': True})

    else:
        form = MessageForm()

    return render(request, 'shpesfba/contact.html', {'form': form})
