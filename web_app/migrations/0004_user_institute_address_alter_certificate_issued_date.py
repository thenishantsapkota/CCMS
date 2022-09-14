# Generated by Django 4.1.1 on 2022-09-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0003_certificate_exam_board"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="institute_address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="certificate",
            name="issued_date",
            field=models.CharField(default="2079-05-29", max_length=200, null=True),
        ),
    ]
