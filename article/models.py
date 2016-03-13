# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User

def create_superuser(sender, **Kwargs):
    if User.objects.filter(username = "admin"):
        return
    User.objects.create_superuser(username = "admin", password = "123456", email = "510195157@qq.com")

post_migrate.connect(create_superuser)

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(verbose_name = "标题", max_length = 100)
    category = models.CharField(verbose_name = "标签", max_length = 50, blank = True)
    content = models.TextField(verbose_name = "正文", blank = True)
    created = models.DateTimeField(verbose_name = "发表时间", auto_now_add = True)
    updated = models.DateTimeField(verbose_name = "更新时间", auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "博客"
        verbose_name_plural = verbose_name