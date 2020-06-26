from rest_framework.serializers import ModelSerializer
from core.models import ReservationControl, Invitation


class ReservationControlSerializer(ModelSerializer):
    class Meta:
        model = ReservationControl
        fields = "__all__"


class InvitationSerializer(ModelSerializer):
    class Meta:
        model = Invitation
        fields = "__all__"


class RSVPPerson(ModelSerializer):
    class Meta:
        model = RSVPPerson
        fields = "__all__"
