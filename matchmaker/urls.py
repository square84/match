from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^question$', 'questions.views.home', name='question_home'),
    url(r'^question/(?P<id>\d+)$', 'questions.views.single', name='question_single'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'matchmaker.views.about', name='about'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$','profiles.views.profile_view', name='profile'),
    url(r'^profile/jobs/add/$', 'profiles.views.job_add', name='job_add'),
    url(r'^profile/jobs/edit/$', 'profiles.views.jobs_edit', name='jobs_update'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)