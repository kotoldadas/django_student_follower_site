# Generated by Django 3.0.5 on 2020-04-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_auto_20200428_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube URL si Giriniz'),
        ),
    ]