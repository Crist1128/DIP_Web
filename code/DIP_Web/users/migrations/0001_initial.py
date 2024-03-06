# Generated by Django 4.1 on 2024-03-06 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("records", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("HospitalName", models.CharField(max_length=255)),
                ("Region", models.CharField(max_length=100)),
                ("Location", models.CharField(max_length=255)),
                (
                    "Catalog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="records.catalog",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hospital",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]