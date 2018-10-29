from django.contrib import admin
from sign.models import Event, Guest
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']  # 定义Event列表需要显示的字段
    search_fields = ['name']  # 添加姓名搜索栏
    list_filter = ['status']  # 添加状态过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'email', 'sign', 'create_time', 'event']  # 定义Gust列表需要显示的字段
    search_fields = ['real_name', 'phone']  # 添加姓名,手机号搜索栏
    list_filter = ['sign']  # 添加登录过滤器


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
