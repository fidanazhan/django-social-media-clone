# Generated by Django 3.1.7 on 2022-07-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220706_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_id',
            field=models.UUIDField(default='62e7e70c', editable=False, primary_key=True, serialize=False),
        ),
    ]
