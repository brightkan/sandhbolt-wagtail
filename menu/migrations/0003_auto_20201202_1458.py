# Generated by Django 3.1.3 on 2020-12-02 14:58

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20201202_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.menu'),
        ),
    ]
