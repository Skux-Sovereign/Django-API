from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
import requests
from rest_framework import status
from rest_framework.response import Response
from scpca_portal.models import Experiment, Sample
from scpca_portal.serializers import (
    SampleSerializer,
    ExperimentListSerializer,
    ExperimentDetailSerializer,
    ExperimentSerializer
)

# Create your views here.
class SampleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class ExperimentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Experiment.objects.all().order_by("-accession")
    ordering_fields = "__all__"
    lookup_field = "accession"


    def get_serializer_class(self):
        if self.action == "list":
            return ExperimentListSerializer
        elif self.action == "retrieve":
            return ExperimentDetailSerializer
        return ExperimentSerializer

    filterset_fields = (
        "accession",
        "metadata",
    )




