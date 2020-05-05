# Generated by Django 3.0.5 on 2020-04-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='phone_number',
            field=models.DecimalField(decimal_places=10, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='final_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='homework',
            name='initial_date',
            field=models.DateField(),
        ),
    ]