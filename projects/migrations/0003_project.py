# Generated by Django 3.1.3 on 2020-12-02 16:02

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectspage_banner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', wagtail.core.fields.RichTextField()),
                ('role', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]