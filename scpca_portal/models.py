from django.db import models
from example_project.models.base import TimestampedModel

class Sample(TimestampedModel):
    class Meta:
        db_table = "samples"
        get_latest_by = "updated_at"
        ordering = ["updated_at"]

    accession = models.TextField(unique=False)
    metadata = models.JSONField(default=dict)
    experiments = models.ManyToManyField(
        "Experiment",
            related_name="sample_related",
            related_query_name="sample",
            blank=True
    )
        
    def __str__(self):
        experiment_accessions = ", ".join([str(experiment.accession) for experiment in self.experiments.all()])
        return f"Sample {self.accession} of Experiments: {experiment_accessions}"
    

class Experiment(TimestampedModel):
    class Meta:
        db_table = "experiments"
        get_latest_by = "updated_at"
        ordering = ["updated_at"]

    accession = models.TextField(unique=False)
    metadata = models.JSONField(default=dict)
    samples = models.ManyToManyField(
        "Sample",
            related_name="experiment_related",
            related_query_name="experiment",
            blank=True
    )

    def __str__(self):
        return f"Experiment {self.accession} ({self.samples.count()} samples)"
    
    def add_sample(self, sample):
        self.samples.add(sample)
        sample.experiments.add(self)