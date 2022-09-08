# Generated by Django 4.1.1 on 2022-09-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog", options={"ordering": ["publish_date"]},
        ),
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/", verbose_name="Resim"
            ),
        ),
    ]