# Generated by Django 4.2.2 on 2023-06-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Area",
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
                ("name", models.CharField(max_length=50, verbose_name="이름")),
            ],
        ),
        migrations.CreateModel(
            name="Spot",
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
                ("type", models.IntegerField(verbose_name="타입")),
                ("title", models.CharField(max_length=200, verbose_name="제목")),
                (
                    "sigungu",
                    models.IntegerField(blank=True, null=True, verbose_name="시군구"),
                ),
                (
                    "addr1",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="주소"
                    ),
                ),
                (
                    "addr2",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="상세주소"
                    ),
                ),
                ("mapx", models.FloatField(verbose_name="x좌표")),
                ("mapy", models.FloatField(verbose_name="y좌표")),
                (
                    "firstimage",
                    models.TextField(blank=True, null=True, verbose_name="이미지"),
                ),
                (
                    "tel",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="전화번호"
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spots",
                        to="spots.area",
                        verbose_name="시도",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sigungu",
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
                ("code", models.IntegerField(default=0, verbose_name="코드")),
                ("name", models.CharField(max_length=50, verbose_name="이름")),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sigungus",
                        to="spots.area",
                        verbose_name="시도",
                    ),
                ),
            ],
        ),
    ]
