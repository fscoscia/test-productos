from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    approved = models.BooleanField("¿Usuario aprobado?", default=False)
    user = models.OneToOneField(
        to=User,
        verbose_name="Usuario",
        on_delete=models.CASCADE,
        related_name="profile",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self) -> str:
        return f"{self.full_name}"
