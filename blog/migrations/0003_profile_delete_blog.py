# Generated by Django 4.1 on 2022-09-08 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_alter_blog_options_blog_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("id_user", models.IntegerField()),
                ("bio", models.TextField(blank=True)),
                (
                    "profileimg",
                    models.ImageField(
                        default="blank-profile-picture.png", upload_to="profile_images"
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="Blog",),
    ]
