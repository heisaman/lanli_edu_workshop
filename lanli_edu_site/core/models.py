from django.contrib.auth.models import AbstractUser
from django.db import models


class School(models.Model):
    name = models.CharField(verbose_name='学校名', max_length=50)
    address = models.CharField(verbose_name='地址', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"学校"
        verbose_name_plural = verbose_name


class Grade(models.Model):
    name = models.CharField(verbose_name='年级名', max_length=50)

    school = models.ForeignKey(School, verbose_name='学校名', related_name='grades')

    def __str__(self):
        return ",".join((self.school.name, self.name))

    class Meta:
        verbose_name = u"年级"
        verbose_name_plural = verbose_name


class Class(models.Model):
    name = models.CharField(verbose_name='班级名', max_length=50)

    grade = models.ForeignKey(Grade, verbose_name='年级名', related_name='classes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"班级"
        verbose_name_plural = verbose_name


class Lecture(models.Model):

    ALL = 0
    SCHOOL = 1
    GRADE = 2
    CLASS = 3
    LEVELS = (
        (ALL, '所有'),
        (SCHOOL, '学校级别'),
        (GRADE, '年级级别'),
        (CLASS, '班级级别'),
    )

    title = models.CharField(verbose_name='标题', max_length=100)
    level = models.IntegerField(verbose_name='级别', choices=LEVELS, default=ALL)
    group_id = models.IntegerField(verbose_name='组织id', null=True)
    content = models.TextField(verbose_name='内容')
    video_url = models.CharField(verbose_name='视频地址', max_length=300)
    expired_time = models.DateTimeField(verbose_name='过期时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"讲座"
        verbose_name_plural = verbose_name


class LanliUser(AbstractUser):

    STUDENT = 1
    TEACHER = 2
    TYPES = (
        (STUDENT, '学生'),
        (TEACHER, '老师')
    )

    MALE = 0
    FEMALE = 1
    UNKNOWN = 2
    SEXES = (
        (MALE, '男'),
        (FEMALE, '女'),
        (UNKNOWN, '未知'),
    )

    COMMON = 'common'
    IN_BLACK_LIST = 'in_black_list'
    STATE_TYPES = (
        (COMMON, '正常'),
        (IN_BLACK_LIST, '已拉入黑名单')
    )

    type = models.IntegerField(verbose_name='身份', choices=TYPES, default=STUDENT)
    sex = models.IntegerField(verbose_name='性别', choices=SEXES, default=MALE)
    nickname = models.CharField(verbose_name='昵称', max_length=50, blank=True)
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    mobile = models.CharField(verbose_name='手机号', max_length=50, blank=True)
    state = models.CharField(verbose_name='会员状态', max_length=40, choices=STATE_TYPES, default=COMMON)
    memo = models.TextField(verbose_name='备注', blank=True)
    money = models.FloatField(verbose_name='余额', default=0)
    last_login_time = models.DateTimeField(verbose_name='上次登录时间', blank=True, null=True)

    attended_class = models.ForeignKey(Class, related_name='attendants', blank=True, null=True)
    attended_lectures = models.ManyToManyField(Lecture, related_name='attendants', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name


class Notification(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    content = models.TextField(verbose_name='内容', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"通知"
        verbose_name_plural = verbose_name
