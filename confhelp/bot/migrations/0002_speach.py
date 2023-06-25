# Generated by Django 4.2.2 on 2023-06-23 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speach",
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
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Наименование"),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("start_at", models.DateTimeField()),
                ("end_at", models.DateTimeField()),
                (
                    "speaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="speachs",
                        to="bot.meetupuser",
                        verbose_name="Спикер",
                    ),
                ),
            ],
        ),
    ]
