from django.conf.urls.defaults import patterns
import os.path

media_root = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = patterns(
    'djangosherd.views',
)
