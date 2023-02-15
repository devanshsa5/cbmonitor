from django.conf.urls import url 
from django.urls import include, re_path, path
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from django.views.static import serve

from webapp.cbmonitor import views


@csrf_exempt
def restful_dispatcher(request, path):
    handler = {
        "add_cluster": views.add_cluster,
        "add_server": views.add_server,
        "add_bucket": views.add_bucket,
        "add_index": views.add_index,
        "add_metric": views.add_metric,
        "add_snapshot": views.add_snapshot,
        "get_clusters": views.get_clusters,
        "get_servers": views.get_servers,
        "get_buckets": views.get_buckets,
        "get_indexes": views.get_indexes,
        "get_snapshots": views.get_snapshots,
        "get_metrics": views.get_metrics,
    }.get(path)
    if handler:
        return handler(request)
    else:
        return HttpResponse(content="Wrong path: {}".format(path), status=404)


urlpatterns = [
    path("favicon\.ico$", RedirectView.as_view(url="/static/favicon.ico")),
    path("reports/html/", views.html_report),
    path("cbmonitor/<str:path>", restful_dispatcher),
]

if settings.DEBUG:
    urlpatterns += [
        url(r"^media/(?P<path>.*)$", serve,
         {"document_root": settings.MEDIA_ROOT})
    ]
