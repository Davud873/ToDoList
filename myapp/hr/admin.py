from django.contrib import admin
from django.db.models import Case, When, Value, IntegerField
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'priority', 'deadline', 'created_at') 
    list_filter = ('completed', 'priority')
    search_fields = ('title', 'description', 'deadline') 

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        priority_order = Case(
            When(priority='high', then=Value(1)),
            When(priority='medium', then=Value(2)),
            When(priority='low', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
        return queryset.annotate(priority_order=priority_order).order_by('priority_order')