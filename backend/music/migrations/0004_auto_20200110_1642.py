# Generated by Django 3.0 on 2020-01-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200107_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='label',
            field=models.ManyToManyField(blank=True, related_name='producer', to='music.Label'),
        ),
    ]
