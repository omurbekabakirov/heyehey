from django.db import models
import random


class ConfirmCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6, null=True, blank=True)

    def generate_code(self):
        self.code = str(random.randint(100000, 999999))
        self.save()
