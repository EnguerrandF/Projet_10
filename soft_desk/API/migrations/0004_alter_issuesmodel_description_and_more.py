# Generated by Django 4.0 on 2023-04-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_issuesmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesmodel',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='issuesmodel',
            name='priority',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='issuesmodel',
            name='tag',
            field=models.CharField(max_length=30, null=True),
        ),
    ]