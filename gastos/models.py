from django.db import models

class Gasto(models.Model):
    descripcion = models.CharField(max_length=100)  # Descripción del gasto
    monto = models.DecimalField(max_digits=10, decimal_places=2)  # Monto del gasto
    fecha = models.DateField(auto_now_add=True)  # Fecha del gasto

    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"
