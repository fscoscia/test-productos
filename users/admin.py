from django.contrib import admin
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin


def approve_user(modelAdmin, request, queryset):
    for user in queryset:
        user.profile.approved = True
        user.profile.save()


approve_user.short_description = "Aprobar usuario"


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "get_approved",
    ]
    list_display_links = [
        "id",
        "username",
        "email",
        "first_name",
    ]
    actions = [
        approve_user,
    ]

    def get_approved(self, obj):
        return obj.profile.approved

    get_approved.boolean = True
    get_approved.short_description = "¿Aprobado?"
    get_approved.admin_order_field = "profile__approved"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
