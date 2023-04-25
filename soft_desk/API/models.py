from django.db import models

from django.db import models
from django.conf import settings


class ProjetsModel(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    type = models.CharField(max_length=128, blank=False, null=False)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )


class ContributorsModel(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    project_id = models.ForeignKey(
        to=ProjetsModel,
        on_delete=models.CASCADE,
    )
    permission = models.BooleanField()
    role = models.CharField(max_length=128)


class IssuesModel(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(max_length=300, blank=False)
    tag = models.CharField(max_length=30, blank=True)
    priority = models.CharField(max_length=128, blank=False)
    projet_id = models.ForeignKey(
        to=ProjetsModel,
        on_delete=models.CASCADE,
        blank=False,
        )
    status = models.BooleanField(blank=False)
    author_user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_user_id",
        blank=False,
        )
    assignee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_user",
        blank=False,
        )
    created_time = models.DateTimeField(
        auto_now_add=True,
    )


class CommentsModel(models.Model):
    description = models.CharField(max_length=300)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    issue_id = models.ForeignKey(
        to=IssuesModel,
        on_delete=models.CASCADE,
        )
    created_time = models.DateTimeField(
        auto_now_add=True
    )
