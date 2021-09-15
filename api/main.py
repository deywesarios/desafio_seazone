from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from clientes.models import Check

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Check
        fields = ["name", "status", "amtpersons", "amtdaily", "location", "publicado", "value"]


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


router = routers.DefaultRouter()
router.register(r'checks', CheckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
