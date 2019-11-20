from django.db import models


from django.db import models
from django.conf import settings
from mainapp.models import Product

class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'Слот корзины'
        verbose_name_plural = 'Слоты корзины'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    created = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.product.name)
# Create your models here.
