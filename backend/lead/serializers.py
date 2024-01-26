from rest_framework import serializers

from .models import Lead

from team.serializers import UserSerializer


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Lead
        read_only_fields = (# fields that generates at backend
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id', # default read-only
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )
