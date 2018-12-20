from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='图书')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.CharField(max_length=200,verbose_name='阅读量')
    bcomment = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0,'男'),
        (1,'女')
    )
    hname = models.CharField(max_length=20,verbose_name='英雄名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES,verbose_name='性别')
    hcomment = models.CharField(max_length=200,null=True,verbose_name='评论量')
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,verbose_name='外键')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_hero'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname