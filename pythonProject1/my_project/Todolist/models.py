from django.db import models
from django.utils import timezone


# 优先级
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('1', '高'),
        ('2', '中'),
        ('3', '低'),
    ]
    # 标题
    title = models.CharField(max_length=200)
    # 内容
    description = models.TextField(blank=True, null=True)
    # 创建日期
    created_date = models.DateTimeField(default=timezone.now)
    # 完成预定
    due_date = models.DateTimeField(blank=True, null=True)
    # 完成与否  Boolean ，default是否 → 未完成
    completed = models.BooleanField(default=False)
    # 优先级 默认是2（中）
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='2')

    def __str__(self):
        return self.title
