# Generated by Django 2.1.11 on 2019-09-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0069_experimentchangelog_changed_vals")]

    operations = [
        migrations.AlterField(
            model_name="experimentvariant",
            name="name",
            field=models.CharField(max_length=255),
        )
    ]
