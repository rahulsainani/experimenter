# Generated by Django 5.1.4 on 2024-12-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0275_nimbusexperiment_firefox_labs_group_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="requires_restart",
            field=models.BooleanField(
                default=False,
                verbose_name="Does this experiment require a restart to take effect? Only used by Firefox Labs.",
            ),
        ),
    ]
