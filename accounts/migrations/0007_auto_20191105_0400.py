# Generated by Django 2.2.4 on 2019-11-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191104_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='injuries',
            field=models.TextField(default='', max_length=1000),
        ),
    ]