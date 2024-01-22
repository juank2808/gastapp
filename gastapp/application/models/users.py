from django.db import models
import bcrypt
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserCustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        print(password)
        if not email:
            raise ValueError('El campo de correo electrónico debe estar configurado.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_birth = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name='last login',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserCustomManager()

    USERNAME_FIELD = ['email','name', 'last_name', 'date_birth']
    REQUIRED_FIELDS = ['name', 'last_name', 'date_birth']

    class Meta:
        db_table = 'application_user'

    def __str__(self):
        return {"email":self.email}
    
    def encrypt_pass(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardarla
        self.set_password(self.password)
        super().save(*args, **kwargs)
    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password)

    def update_user(self, name=None, last_name=None, date_birth=None):
        if name:
            self.name = name
        if last_name:
            self.last_name = last_name
        if date_birth:
            self.date_birth = date_birth
        self.save()
