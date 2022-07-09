# Generated by Django 3.1.7 on 2022-07-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_types',
            field=models.IntegerField(choices=[(1, 'Like'), (2, 'Share'), (3, 'PostComment'), (4, 'CommentReply'), (5, 'Follow')]),
        ),
    ]
