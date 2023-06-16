# Generated by Django 4.2.1 on 2023-06-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listing_is_closed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
