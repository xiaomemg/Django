from django.contrib import admin

# Register your models here.
from demo_table.models import BookInfo, HeroInfo

# 创建一个新的类,建立关联对象
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1 # 附加要编辑的数量

# 可以使用表格形式嵌入
class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    # 分页
    list_per_page = 3
    # 列表
    list_display = ['id','btitle','bpub_date']
    # 过滤器
    list_filter = ['btitle']
    # 搜索条
    search_fields = ['btitle']
    # 显示每个图书的显示的字段
    # fields = ['btitle','bpub_date']
    fieldsets = (
        ('基础', {'fields': ('btitle', 'bpub_date')}),
        ('高级', {'fields': ('bread', 'bcomment'),
                'classes': ('collapse',) # 表示是否折叠
                })
    )
    inlines = [HeroInfoStackInline]
    inlines = [HeroInfoTabularInline]

class HeroInfoAdmin(admin.ModelAdmin):
    # 分页
    list_per_page = 6
    # 列表
    list_display = ['id','hname','hgender','read']
    # 过滤器
    list_filter = ['hname','hgender']
    # 搜索条
    search_fields = ['hname','hgender']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.site_header = '网上书城'
admin.site.site_title = '免费书城'
admin.site.index_title = '欢迎进入书城世界'