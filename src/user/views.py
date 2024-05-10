from base.views import BaseViewSet
from src.user import filters, serializers
from src.user.models import User


class UserViewSet(BaseViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.exclude(is_superuser=True).all()
    filterset_class = filters.UserFilter
    http_method_names = ["get", "post", "patch", "put"]
    no_permission_method = []

