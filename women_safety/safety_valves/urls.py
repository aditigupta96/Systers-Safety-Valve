from django.conf.urls import url
from django.contrib import admin
from .views import (complaint, 
	               complaint_feed,
	               share_incident,
	               share_twitter, 
	               complaint_details, 
	               my_complaints, 
	               safety_tips, 
	               email)

urlpatterns = [
    url(r'^add/$', complaint, name='add-complaint'),
    url(r'^feed/$', complaint_feed, name='complaint-feed'),
    url(r'^share/(?P<id>\d+)/$', share_incident, name='share-incident'),
    url(r'^sharetwitter/(?P<id>\d+)/$', share_twitter),
    url(r'^email/(?P<id>\d+)/$', email),
    url(r'detail/(?P<id>\d+)/$', complaint_details, name="complaint-details"),
    url(r'^mycomplaints/$', my_complaints, name='my-complaints'),
    url(r'^safetytips/$', safety_tips, name='safety-tips'),
]
