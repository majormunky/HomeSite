# Generated by Django 3.0.8 on 2020-07-31 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]