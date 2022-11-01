from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project import settings
# Import for the JWT
from rest_framework_simplejwt import views as jwt_views
# Import for the API Docs
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Motion Backend",
      default_version='v1',
      description="Manuel's Motion Social Media App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="learn@propulsionacademy.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True, # Set to False restrict access to protected endpoints
   permission_classes=(permissions.AllowAny,), # Permissions for docs access
)


urlpatterns = [
    path('backend/api/admin/', admin.site.urls),
    path('backend/api/social/posts/', include("post.urls")),
    path('backend/api/', include("user.urls")),
    # URLs for the JWT. To get a token go to /token.
    path('backend/api/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/api/auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),
    # URL for the API Docs
    path('backend/api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# current token superuser eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NTA1ODgyLCJpYXQiOjE2NjUzMzMwODIsImp0aSI6IjYxNTc2ZTU0MDAzZTRjZmQ5ZWFiOWRiNmY3NGVjNzYwIiwidXNlcl9pZCI6MX0.tF4lc-QjKwBD8CtrU4cxHsYerGZZZzJIIsjsLhmhkFc
# current token dummy user eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1MzIwODg4LCJpYXQiOjE2NjUxNDgwODgsImp0aSI6ImEwYTRlZTdiMzFlMzRlNjk4OGNlMGE2MGJkMWY0MDJjIiwidXNlcl9pZCI6Mn0.ukOibMlexbQGZRJv2ZX8PkD6SzWBH-WGcaegXDWP2S4

# code to display post Image in admin
if settings.DEBUG:  # we only want to add these urls in debug mode. You will learn about serving in production next week
    ...
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)