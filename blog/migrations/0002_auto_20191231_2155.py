# Generated by Django 2.2.4 on 2019-12-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]