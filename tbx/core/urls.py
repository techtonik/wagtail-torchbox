from django.conf.urls import url

from tbx.core.feeds import BlogFeed, PlanetDrupalFeed
from tbx.core import views

urlpatterns = [
    url(r'^blog/feed/$', BlogFeed(), name='blog_feed'),
    url(r'^newsletter-subscribe', views.newsletter_subsribe),
    url(
        r'^planet_drupal_feed/$',
        PlanetDrupalFeed(),
        name='planet_drupal_feed'
    ),
]
