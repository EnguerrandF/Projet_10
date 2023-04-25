from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from authentication.models import UserModel
from API.models import ProjetsModel, ContributorsModel, IssuesModel, CommentsModel
from API.serializer import ProjetsSerializer, ProjetsDetailSerializer,\
    ContributorsSerializer, IssuesDetailSerializer, IssuesSerializer, CommentsSerializer


class ProjetsView(viewsets.ModelViewSet):
    serializer_class = ProjetsSerializer
    detail_serializer_class = ProjetsDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProjetsModel.objects.filter(author_user_id=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['author_user_id'] = self.request.user.id
        serializer = self.detail_serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author_user_id=self.request.user)

        return Response(serializer.data)

    def update(self, *args, **kwargs):
        instance = self.get_object()
        validated_data = self.request.data

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContributorsView(viewsets.ModelViewSet):
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, projet_pk):
        contributors = ContributorsModel.objects.filter(project_id=projet_pk)
        serializer = ContributorsSerializer(contributors, many=True)
        return Response(serializer.data)

    def create(self, request, projet_pk):
        data = request.data.copy()
        if UserModel.objects.filter(username=data['user_id']):
            data['user_id'] = UserModel.objects.get(username=data['user_id']).id
            data['project_id'] = ProjetsModel.objects.get(id=projet_pk).id

            serializer = ContributorsSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={data["user_id"]: 'Utilisateur non valide'})

    def destroy(self, request, projet_pk, pk):
        model_contributor = ContributorsModel.objects.get(id=pk)
        model_contributor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssuesView(viewsets.ModelViewSet):
    serializer_class = IssuesSerializer
    detail_serializer_class = IssuesDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = IssuesModel.objects.all()

    def list(self, request, projet_pk):
        issues = IssuesModel.objects.filter(projet_id=projet_pk)
        serializer = self.serializer_class(issues, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, projet_pk):
        data = request.data.copy()
        if UserModel.objects.filter(username=data['assignee_user']):
            data['assignee_user'] = UserModel.objects.get(username=data['assignee_user']).id
            data['author_user_id'] = self.request.user.id
            data['projet_id'] = ProjetsModel.objects.get(id=projet_pk).id

            serializer = self.detail_serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={data["assignee_user"]: 'Utilisateur non valide'})

    def update(self, request, projet_pk, pk):
        instance = self.get_object()
        validated_data = self.request.data

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.status = validated_data.get('status', instance.status)
        if UserModel.objects.filter(username=validated_data.get("assignee_user")):
            print("UUUUUUUUUUUUUUUUUUU", validated_data.get("assignee_user"))
            instance.assignee_user = validated_data.get(UserModel.objects.get(username=validated_data.get("assignee_user")).id)
            print(instance.assignee_user, "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={validated_data["assignee_user"]: 'Utilisateur non valide'})

        instance.save()

        serializer = self.detail_serializer_class(instance)
        return Response(serializer.data)

    def destroy(self, request, projet_pk, pk):
        model_issues = IssuesModel.objects.get(id=pk)
        model_issues.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
    queryset = CommentsModel.objects.all()

    def list(self, request, projet_pk, issue_pk):
        issues = CommentsModel.objects.filter(issue_id=issue_pk)
        serializer = self.serializer_class(issues, many=True)
        return Response(serializer.data)

    def create(self, request, projet_pk, issue_pk):
        data = request.data.copy()
        data['author_user'] = self.request.user.id
        data['issue_id'] = IssuesModel.objects.get(id=issue_pk).id
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, projet_pk, issue_pk, pk):
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO", projet_pk, issue_pk, pk)
        instance = self.get_object()
        validated_data = self.request.data

        instance.description = validated_data.get('description', instance.description)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, projet_pk, issue_pk, pk):
        model_issues = CommentsModel.objects.get(id=pk)
        model_issues.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)