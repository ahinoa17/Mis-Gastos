from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField("Descripción", max_length=120)
    monto = models.DecimalField("Monto", max_digits=8, decimal_places=2)
    fecha = models.DateField("Fecha", auto_now_add=True)

    def __str__(self):
        return f"{self.descripcion} - ${self.monto:.2f}"

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
        ordering = ["-fecha", "-id"]