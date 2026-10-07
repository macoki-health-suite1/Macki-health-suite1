"""Tenant isolation: users only ever see and write data for their own organisation."""
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

TENANT_READ_ONLY = ("organisation", "facility", "created_at", "updated_at")


class TenantSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        org_id = self.context["request"].user.organisation_id
        for value in attrs.values():
            if hasattr(value, "organisation_id") and value.organisation_id != org_id:
                raise serializers.ValidationError(
                    "Related record belongs to another organisation."
                )
        return attrs


class TenantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        org_id = getattr(self.request.user, "organisation_id", None)
        qs = super().get_queryset()
        if org_id is None:
            return qs.none()
        return qs.filter(organisation_id=org_id)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(organisation=user.organisation, facility=user.facility)
