from rest_framework.serializers import ModelSerializer

from API.models import ProjetsModel, ContributorsModel, IssuesModel, CommentsModel


class ProjetsSerializer(ModelSerializer):
    class Meta:
        model = ProjetsModel
        fields = ['id', "title"]


class ProjetsDetailSerializer(ModelSerializer):
    class Meta:
        model = ProjetsModel
        fields = ['id', 'title', 'description', 'type', 'author_user_id']


class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = ContributorsModel
        fields = ["id", "permission", "role", "user_id", "project_id"]


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = IssuesModel
        fields = ["id", 'title']


class IssuesDetailSerializer(ModelSerializer):
    class Meta:
        model = IssuesModel
        fields = ["id", "title", "description", "tag", "priority", "projet_id",
                  "status", "author_user_id", "assignee_user", "created_time"]


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ["id", "description", "author_user", "issue_id"]
