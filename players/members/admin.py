from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

# Register the Member model with the MemberAdmin configuration
admin.site.register(Member, MemberAdmin)
