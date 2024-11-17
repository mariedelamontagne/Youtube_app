# Generated by Django 5.1.3 on 2024-11-17 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_remove_youtubevideo_date_uploaded'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
