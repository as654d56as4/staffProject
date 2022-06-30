from django.db import models


# Create your models here.


class Admin(models.Model):
    '''管理员'''
    username=models.CharField(verbose_name='姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
class Department(models.Model):
    ''' 部门表 '''
    industry_title = models.CharField(verbose_name='部门标题', max_length=32)

    def __str__(self):
        return self.industry_title  # 将对象转化为文本输出


class staff(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',
                                  max_digits=10,  # 数字长度为10
                                  decimal_places=2,  # 小数位为2
                                  default=0)
    # create_time = models.DateTimeField(verbose_name='入职时间', auto_now_add=True)
    # create_time = models.DateTimeField(verbose_name='入职时间',null=True,blank=True)
    create_time = models.DateField(verbose_name='入职时间',null=True,blank=True)
    phone = models.ForeignKey(to='beautyPhone',verbose_name='手机号',on_delete=models.CASCADE,null=True,blank=True)
    # 数据库无约束(不推荐)
    # department_id = models.IntegerField(verbose_name='部门id')
    # 数据库有约束 to='需要关联的表'  to_field='对表中的某一个字段做关联'
    # Django内部使用 models.ForeignKey 生成表时自动将字段名变为 “当前字段名”+ "_id"
    # 部门表被删除
    # 级联删除
    department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
    # 部门ID字段为空
    # department = models.ForeignKey(to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)
    gender_choices = (  # Django中的约束
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class beautyPhone(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name='手机号',max_length=32)
    price = models.IntegerField(verbose_name='价格')
    rank_choices=(
        (1,'免费用户'),
        (2,'vip'),
        (3,'Svip')
    )
    rank = models.SmallIntegerField(verbose_name='级别',choices=rank_choices,default=1)
    status_choices=(
        (0,'未使用'),
        (1,'已占用')
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=0)