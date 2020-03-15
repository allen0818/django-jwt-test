from django.db import models
from django.contrib.auth.models import AbstractUser

# 如果擴展或替換 Django 預設用的 User Model，
# 記得在 settings.py 中設定:
# AUTH_USER_MODEL = 'myapp.MyUser'

# AbstractUser     : 欄位可參考資料庫內的 auth_user 資料表
# AbstractBaseUser : 欄位預設只有 password, last_login, is_active
class User(AbstractUser):
    # append custom fields
    phone = models.CharField(max_length=50, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username