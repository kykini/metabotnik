from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^$', 'metabotnik.views.home', name='home'),
    url(r'^help/(\w+)$', 'metabotnik.views.help', name='help'),

    url(r'^folders/$', 'metabotnik.views.folders', name='folders'),
    url(r'^projects/$', 'metabotnik.views.projects', name='projects'),
    url(r'^projects/([0-9]+)/$', 'metabotnik.views.project', name='project'),
    url(r'^projects/([0-9]+)/generate$', 'metabotnik.views.generate', name='generate'),
    url(r'^projects/([0-9]+)/delete$', 'metabotnik.views.delete_project', name='delete_project'),
    
    url(r'^projects/([0-9]+)/(\w+)/(preview)\.jpg$', 'metabotnik.views.projectpreview', name='preview'),
    url(r'^projects/([0-9]+)/(\w+)/(metabotnik)\.jpg$', 'metabotnik.views.projectpreview', name='metabotnik'),

    # Authentication
    url(r'^login$', 'metabotnik.auth.loginview', name='login'),
    url(r'^logout$', 'metabotnik.auth.logoutview', name='logout'),
    url(r'^dropboxauthredirect$', 'metabotnik.auth.dropboxauthredirect', name='dropboxauthredirect'),

    url(r'^admin/', include(admin.site.urls)),
)
