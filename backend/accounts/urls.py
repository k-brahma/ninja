from django.urls import path

from ninja import NinjaAPI

from .views import auth_router

api = NinjaAPI(title="Accounts API", urls_namespace="accounts_api")
api.add_router("/auth/", auth_router)

urlpatterns = [
    path("", api.urls),
]
