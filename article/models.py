# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 标题，CharField为字符串字段，用于保存较短的字符串
    title = models.CharField(max_length=100)
    # 文章正文，保存大量文本使用TextField
    body = models.TextField()
    # 创建时间，创建时默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间，每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self) -> str:
        return self.title

