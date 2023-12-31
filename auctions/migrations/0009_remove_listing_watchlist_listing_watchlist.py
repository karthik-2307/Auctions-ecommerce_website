# Generated by Django 4.2.1 on 2023-06-07 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='watch_listings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
