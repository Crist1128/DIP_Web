from django.db import models

# 定义Catalog模型，代表DIP目录表，存储目录相关信息
class Catalog(models.Model):
    CatalogID = models.AutoField(primary_key=True)  # 自动增长的主键
    CatalogName = models.CharField(max_length=255)  # 目录名称
    CatalogDescription = models.TextField(blank=True, null=True)  # 目录描述，可选字段
    CreationDate = models.DateTimeField()  # 创建日期
    LastModifiedDate = models.DateTimeField()  # 最后修改日期

    def __str__(self):
        return self.CatalogName  # 对象的字符串表示形式为目录名称

# 定义Diagnosis模型，存储诊断信息
class Diagnosis(models.Model):
    DiagnosisID = models.AutoField(primary_key=True)  # 自动增长的主键
    DiagnosisCode = models.CharField(max_length=20)  # 诊断代码
    DiagnosisName = models.CharField(max_length=255, blank=True, null=True)  # 诊断名称，可选字段
    Catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)  # 外键，关联到Catalog模型

    def __str__(self):
        return self.DiagnosisName  # 对象的字符串表示形式为诊断名称

# 定义Procedure模型，存储操作程序信息
class Procedure(models.Model):
    ProcedureID = models.AutoField(primary_key=True)  # 自动增长的主键
    ProcedureCode = models.CharField(max_length=20)  # 操作程序代码
    ProcedureName = models.CharField(max_length=255, blank=True, null=True)  # 操作程序名称，可选字段
    Catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)  # 外键，关联到Catalog模型

    def __str__(self):
        return self.ProcedureName  # 对象的字符串表示形式为操作程序名称

# 定义Scoring模型，存储评分信息
class Scoring(models.Model):
    ScoringID = models.AutoField(primary_key=True)  # 自动增长的主键
    Diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)  # 外键，关联到Diagnosis模型
    ProcedureCodes = models.TextField(blank=True, null=True)  # 操作程序代码，可以包含多个代码
    ScoringValue = models.IntegerField()  # 评分值
    Catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)  # 外键，关联到Catalog模型
