from django.contrib import admin

# Register your models here.

from .models import Grades,Students

#注册
class GradesAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加、修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ]

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['pk','sname','sage','sgender','scontend','sgrade','isDelete']
    list_per_page = 2

admin.site.register(Grades,GradesAdmin)         #使用自定义管理界面
admin.site.register(Students,StudentsAdmin)