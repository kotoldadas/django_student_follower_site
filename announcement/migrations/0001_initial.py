# Generated by Django 3.0.5 on 2020-04-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulan Zaman')),
            ],
        ),
    ]
