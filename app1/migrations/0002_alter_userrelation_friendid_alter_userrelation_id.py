# Generated by Django 4.2.5 on 2023-09-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrelation',
            name='friendid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]