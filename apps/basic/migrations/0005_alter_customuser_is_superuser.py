# Generated by Django 4.2.3 on 2023-08-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0004_alter_customuser_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
