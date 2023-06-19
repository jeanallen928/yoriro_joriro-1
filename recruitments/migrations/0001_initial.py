# Generated by Django 4.2.2 on 2023-06-19 15:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recruitments",
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
                ("title", models.CharField(max_length=50, verbose_name="제목")),
                ("place", models.CharField(max_length=128, verbose_name="여행지")),
                ("cost", models.PositiveIntegerField(verbose_name="경비")),
                ("content", models.TextField(verbose_name="내용")),
                ("departure", models.DateTimeField(verbose_name="출발일")),
                ("arrival", models.DateTimeField(verbose_name="도착일")),
                (
                    "participant_max",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(2),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="모집 정원",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                (
                    "is_complete",
                    models.IntegerField(
                        choices=[(0, "모집중"), (1, "모집완료"), (2, "여행중"), (3, "여행완료")],
                        default=0,
                        verbose_name="모집 완료 여부",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="recruitments/%Y/%m/", verbose_name="이미지"
                    ),
                ),
                (
                    "participant",
                    models.ManyToManyField(
                        blank=True,
                        related_name="participant",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="참가자",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="유저",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Applicant",
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
                ("appeal", models.CharField(max_length=128, verbose_name="포부")),
                (
                    "acceptence",
                    models.IntegerField(
                        choices=[(0, "대기중"), (1, "거절"), (2, "수락")],
                        default=0,
                        verbose_name="합격 여부",
                    ),
                ),
                (
                    "recruitment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recruitments.recruitments",
                        verbose_name="동료 모집",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="신청자",
                    ),
                ),
            ],
        ),
    ]
