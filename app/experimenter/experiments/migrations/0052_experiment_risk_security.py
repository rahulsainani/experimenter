# Generated by Django 2.1.7 on 2019-04-29 17:25

from django.db import migrations, models
from experimenter.experiments.constants import ExperimentConstants


def populate_risk_security(apps, schema_editor):
    Experiment = apps.get_model("experiments", "Experiment")
    filtered_experiments = Experiment.objects.filter(
        status__in=[
            ExperimentConstants.STATUS_SHIP,
            ExperimentConstants.STATUS_ACCEPTED,
            ExperimentConstants.STATUS_LIVE,
            ExperimentConstants.STATUS_COMPLETE,
            "Rejected",
        ]
    )
    filtered_experiments.filter(risk_security=None).update(risk_security=False)


class Migration(migrations.Migration):

    dependencies = [("experiments", "0051_experiment_risk_ux")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="risk_security",
            field=models.NullBooleanField(default=None),
        ),
        migrations.RunPython(populate_risk_security),
    ]
