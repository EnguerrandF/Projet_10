from rest_framework.permissions import BasePermission
from rest_framework import permissions

from API.models import ContributorsModel, ProjetsModel, IssuesModel, CommentsModel


class ProjetsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            pk = view.kwargs["pk"]
            if ProjetsModel.objects.filter(author_user_id=request.user, id=pk):
                return True


class ContributorsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.method == "GET":
                return True
        else:
            projet_pk = view.kwargs["projet_pk"]
            if request.method == 'DELETE':
                if ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk):
                    return True
            elif request.method == 'POST':
                print(projet_pk, request.user)
                if ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk):
                    return True


class IssuesPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.method == 'GET':
                projet_pk = view.kwargs["projet_pk"]
                if (ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk) or
                        ContributorsModel.objects.filter(user_id=request.user, project_id=projet_pk)):
                    return True
        else:
            if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
                projet_pk = view.kwargs["projet_pk"]
                if ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk):
                    return True


class CommentsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.method == 'GET':
                projet_pk = view.kwargs["projet_pk"]
                if (ContributorsModel.objects.filter(user_id=request.user, project_id=projet_pk) or
                        ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk)):
                    return True
        else:
            if request.method == 'POST':
                projet_pk = view.kwargs["projet_pk"]
                if (ContributorsModel.objects.filter(user_id=request.user, project_id=projet_pk) or
                        ProjetsModel.objects.filter(author_user_id=request.user, id=projet_pk)):
                    return True
            elif request.method == 'DELETE' or request.method == 'PUT':
                pk = view.kwargs["pk"]
                if CommentsModel.objects.filter(id=pk, author_user=request.user):
                    return True
