from django.db import models
from django.contrib.auth.models import User
from records.models import Catalog  # 从records app导入Catalog模型

# 定义Hospital模型，存储医院用户信息
class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital')  # 与Django内置的User模型建立一对一关系
    HospitalName = models.CharField(max_length=255)  # 医院名称
    Region = models.CharField(max_length=100)  # 所属地区
    Location = models.CharField(max_length=255)  # 准确位置
    Catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True, blank=True)  # 可选的外键，关联到Catalog模型

    def __str__(self):
        return self.HospitalName  # 对象的字符串表示形式为医院名称
