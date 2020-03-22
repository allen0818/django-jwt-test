from django.db import models
from django.contrib.auth.models import AbstractUser

# 記得在 settings.py 中設定:
# AUTH_USER_MODEL = 'myapp.MyUser'
class User(AbstractUser):
    # append custom fields
    phone = models.CharField(max_length=50, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username