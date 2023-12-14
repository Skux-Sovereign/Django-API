from rest_framework import serializers
from scpca_portal.models import Experiment, Sample

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"


class ExperimentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = (
            "id",
            "accession",
            "metadata",
        )

class ExperimentDetailSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True, read_only=True)

    class Meta:
        model = Experiment
        fields = (
            "accession",
            "metadata",
            "samples",
        )

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = (
            "accession",
            "metadata",
            "samples",
        )