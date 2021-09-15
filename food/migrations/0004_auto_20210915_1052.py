# Generated by Django 3.2.7 on 2021-09-15 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_alter_food_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='dish',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='food',
            name='customer',
        ),
        migrations.AddField(
            model_name='food',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='hourly_sales',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='food',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]