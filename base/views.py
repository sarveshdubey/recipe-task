from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from . import mixins
from .helpers import get_response_message


class BaseViewSet(mixins.ViewSetMixin, viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    http_method_names = ["get", "post", "patch", "delete", "put"]
    no_permission_method = []

    model = None
    filterset_class = None
    lookup_field = "id"

    def get_permissions(self):
        if self.action in self.no_permission_method:
            # Disable authentication for create action
            return []
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        response = {
            "response_data": response_data,
            "message": get_response_message(response_data, self.model, self.action),
        }
        return Response(data=response, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        response_data = serializer.data
        action_name = self.action
        if partial:
            action_name = "update"
        response = {
            "response_data": response_data,
            "message": get_response_message(response_data, self.model, action_name),
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Deleted successfully"})

