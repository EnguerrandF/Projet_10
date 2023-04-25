from django.contrib import admin
from API.models import ProjetsModel, ContributorsModel, IssuesModel, CommentsModel


class ProjetModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type')


class ContributorModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'project_id', 'permission', 'role')


class IssuesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'priority', 'status')


class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ("description", "author_user", "issue_id")


admin.site.register(ProjetsModel, ProjetModelAdmin)
admin.site.register(ContributorsModel, ContributorModelAdmin)
admin.site.register(IssuesModel, IssuesModelAdmin)
admin.site.register(CommentsModel, CommentsModelAdmin)
