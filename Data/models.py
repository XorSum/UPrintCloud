from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='邮箱',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(verbose_name='用户昵称', max_length=32)
    is_active = models.BooleanField(verbose_name='用户可用', default=True)
    is_admin = models.BooleanField(verbose_name='管理员用户', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class RabbitMQNode(models.Model):
    url = models.CharField(verbose_name='节点地址', max_length=32, primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=10)
    password = models.CharField(verbose_name='密码', max_length=32)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = '节点'


class Client(models.Model):
    id = models.CharField(verbose_name='终端识别号', max_length=11, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='所属用户')
    rabbitmq_node = models.ForeignKey(RabbitMQNode, on_delete=models.PROTECT, verbose_name='依赖节点')

    class Meta:
        verbose_name = '终端'
        verbose_name_plural = '终端'


class Job(models.Model):
    id = models.CharField(verbose_name='任务编号', max_length=30, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='所属用户')
    file = models.FileField(verbose_name='文件', upload_to='static/usr/uploads/files/%Y/%m/%d/')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    finished = models.BooleanField(verbose_name='已经打印', default=False)
    finished_date = models.DateTimeField(verbose_name='打印日期', auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='打印终端', null=True)

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'
        ordering=['-create_date']



