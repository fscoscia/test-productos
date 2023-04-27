from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    NOT_AVAILABLE = 0
    AVAILABLE = 1
    STATE_CHOICES = ((NOT_AVAILABLE, "No disponible"), (AVAILABLE, "Disponible"))

    name = models.CharField(verbose_name="Nombre", max_length=150)
    state = models.PositiveSmallIntegerField(
        verbose_name="Estado", choices=STATE_CHOICES, default=AVAILABLE
    )
    categories = models.ManyToManyField(
        to=Category,
        verbose_name="Categorías",
        related_name="products",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return f"{self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Producto",
    )

    image = models.ImageField(verbose_name="Imagen", upload_to="products/images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imagen de producto"
        verbose_name_plural = "Imágenes de productos"
