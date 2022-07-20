from django.urls import path, include
from rest_framework import routers
from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'procedures', views.ProcedureViewSet)
router.register(r'instructions', views.InstructionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('api/procedurelist/<username>/', views.ProcedureList.as_view()),
    path('api/instructionlist/<username>/<procedure_id>/', views.InstructionList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

