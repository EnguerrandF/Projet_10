# Generated by Django 4.0 on 2023-04-22 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('API', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetsmodel',
            name='author_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodel'),
        ),
        migrations.AddField(
            model_name='issuesmodel',
            name='assignee_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user', to='authentication.usermodel'),
        ),
        migrations.AddField(
            model_name='issuesmodel',
            name='author_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_user_id', to='authentication.usermodel'),
        ),
        migrations.AddField(
            model_name='issuesmodel',
            name='projet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.projetsmodel'),
        ),
        migrations.AddField(
            model_name='contributorsmodel',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.projetsmodel'),
        ),
        migrations.AddField(
            model_name='contributorsmodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodel'),
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='author_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.usermodel'),
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='issue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.issuesmodel'),
        ),
    ]