from django.contrib import admin
from django.urls import path, include
# from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
import dj_rest_auth.views
# from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# schema_view = get_schema_view(
#     openapi.Info(
#         title="2Meiget API Documentation",
#         default_version='v1',
#     ),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('dj_rest_auth.urls')),
    path('account/register/', include('dj_rest_auth.registration.urls')),
    # path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
    #      name='schema-swagger-ui'),
    path('', include('users.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()