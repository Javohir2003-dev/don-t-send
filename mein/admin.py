from django.contrib import admin # type: ignore
from .models import Student,Group,Belgi,Davomat


admin.site.register([Student, Belgi, Davomat])




class StudentInline(admin.TabularInline):
    model = Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

    
