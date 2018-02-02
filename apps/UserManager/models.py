from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserAccount(AbstractUser):
    """继承系统用户表"""
    uid = models.AutoField(primary_key=True, verbose_name=u'用户uid')
    avatar_file = models.ImageField(upload_to='img/%Y/%m/%d/', default=u'img/avatar1.png',
                                    verbose_name=u'用户头像')

    def __str__(self):
        return self.username

    def user_role(self):
        # 返回用户角色名
        return RolesDetail.objects.annotate(role_name=F('role__role_name')).get(user__uid=1).role_name

    class Meta:
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_useraccount'


class Roles(models.Model):
    """用户角色表"""
    role_id = models.AutoField(primary_key=True, verbose_name=u'主键')
    role_name = models.CharField(max_length=30, null=False, verbose_name=u'角色名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = u'用户角色表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_roles'


class RolesDetail(models.Model):
    """用户角色详情表"""
    id = models.AutoField(primary_key=True, verbose_name=u'主键')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'用户角色详情表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_roles_detail'

        unique_together = ('user',)


class Groups(models.Model):
    """
    用户组表
    """
    group_id = models.AutoField(primary_key=True, verbose_name=u'主键')
    group_name = models.CharField(max_length=30, default='', verbose_name=u'组名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = u'用户组表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_groups'


class GroupsDetail(models.Model):
    """用户组详情表"""
    id = models.AutoField(primary_key=True, verbose_name=u'主键')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'用户组详情表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_groups_detail'

        unique_together = ('user',)


class Contacts(models.Model):
    """联系人表"""
    contact_id = models.AutoField(primary_key=True, verbose_name=u'主键')
    contact_name = models.CharField(max_length=30, default='', verbose_name=u'联系人姓名')
    contact_email = models.EmailField(max_length=128, default='', verbose_name=u'联系人邮箱')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = u'联系人表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'auditsql_contacts'

        unique_together = ('contact_name', 'contact_email')
