# Generated by Django 4.2.2 on 2024-02-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=128)),
                ("price", models.DecimalField(decimal_places=2, max_digits=16)),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=1)),
            ],
        ),
    ]
