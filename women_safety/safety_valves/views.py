from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ComplaintForm
from .models import Complaint
from .utils import post_to_twitter, send_email
from django_countries import countries

@login_required(login_url='/login/')
def complaint(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title'] # equivalent to request.POST.get('title', None)
        company = request.POST['company']
        person = request.POST['person']
        city = request.POST['city']
        country = request.POST['country']
        experience = request.POST['experience']
        
        complaint = Complaint(user=user, title=title, company=company, person=person, city=city,
        	                  country=country, experience=experience)
        complaint.save()
        return redirect('share-incident', id=complaint.id)

    else:
        return render(request, 'safety_valves/complaint_form.html', {'countries': countries, 'user': request.user})

def complaint_feed(request):
    feed = Complaint.objects.all()[:10]
    return render(request, 'safety_valves/complaint_feed.html', {'feed': feed, 'user': request.user})

@login_required(login_url='/login/')
def share_incident(request, id):
    incident = Complaint.objects.get(pk=id)
    recipient_list = ['agarwalm214@gmail.com', 'aditi.medha96@gmail.com']
    if request.user == incident.user or request.user.is_superuser:
        return render(request, 'safety_valves/share_incident.html', {'incident': incident, 'user': request.user, 'emails': recipient_list})
    else:
        return HttpResponse("Forbidden")

@login_required(login_url='/login/')
def share_twitter(request, id):
    url = "https://127.0.0.1:8000/complaint/" + id
    post_to_twitter(url)
    return redirect('share-incident', id=id)

@login_required(login_url='/login/')
def email(request, id):
    if request.method == "POST":
        incident = Complaint.objects.get(pk=id)
        messages = []
        from_email = "Systers Safety"
        subject = incident.title
        message = incident.experience
        
        recipient_list = map(str, request.POST.getlist("checks"))
        print recipient_list
        for i in recipient_list:
            to = []
            to.append(i)
            temp_message = (subject, message, from_email, to)
            messages.append(temp_message)

        send_email(messages)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("GET method not allowed")

def complaint_details(request, id):
    incident = Complaint.objects.get(pk=id)
    return render(request, 'safety_valves/complaint_details.html', {'incident': incident, 'user': request.user})

@login_required(login_url='/login/')
def my_complaints(request):
    feed = Complaint.objects.all().filter(user=request.user)
    return render(request, 'safety_valves/my_complaints.html', {'feed': feed, 'user': request.user})

def safety_tips(request):
    return render(request, 'safety_valves/safety_tips.html')
