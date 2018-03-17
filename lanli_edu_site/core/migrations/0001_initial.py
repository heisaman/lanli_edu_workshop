# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-17 08:21
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanliUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.IntegerField(choices=[(1, '学生'), (2, '老师')], default=1, verbose_name='身份')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=0, verbose_name='性别')),
                ('nickname', models.CharField(blank=True, max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(null=True, verbose_name='生日')),
                ('mobile', models.CharField(blank=True, max_length=50, verbose_name='手机号')),
                ('state', models.CharField(choices=[('common', '正常'), ('in_black_list', '已拉入黑名单')], default='common', max_length=40, verbose_name='会员状态')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('money', models.FloatField(default=0, verbose_name='余额')),
                ('last_login_time', models.DateTimeField(null=True, verbose_name='上次登录时间')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='班级名')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='年级名')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('level', models.IntegerField(choices=[(0, '所有'), (1, '学校级别'), (2, '年级级别'), (3, '班级级别')], default=0, verbose_name='级别')),
                ('group_id', models.IntegerField(null=True, verbose_name='组织id')),
                ('content', models.TextField(verbose_name='内容')),
                ('video_url', models.CharField(max_length=300, verbose_name='视频地址')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(blank=True, verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学校名')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='core.School'),
        ),
        migrations.AddField(
            model_name='class',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='core.Grade'),
        ),
        migrations.AddField(
            model_name='lanliuser',
            name='attended_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendants', to='core.Class'),
        ),
        migrations.AddField(
            model_name='lanliuser',
            name='attended_lectures',
            field=models.ManyToManyField(related_name='attendants', to='core.Lecture'),
        ),
        migrations.AddField(
            model_name='lanliuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='lanliuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
