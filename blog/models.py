from django.db import models

# Create your models here.

#创建一个表
class Person(models.Model):
    #表中的一个字段
    first_name=models.CharField('第一个名字',max_length=200)
    last_name=models.CharField('第二个名字',max_length=30)
    #email类型的，会自动校验该字段是否是合法的email
    email=models.EmailField('邮箱')
    #新添加数据的时候，注册时，，会有当前时间的值
    create_at=models.DateField(auto_now_add=True)
    #更新的时候该时间字段会更新该数据的值为现在的时间
    update_at=models.DateField(auto_now=True)