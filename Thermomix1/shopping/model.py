#encoding:utf-8


from django.db import models
from django.utils.translation import ugettext as _
from recipes.models import Ingredients

# Unidades (Kg,g,l,etc.)
class ShoppingList(models.Model):    
    name = models.CharField(_(u'Nombre'),max_length=100)
    creation_date = models.DateField(_(u'Fecha de creación'))
    made_date = models.DateField(_(u'Fecha de compra'))
    made = models.BooleanField(_(u'Compra realizada'),default=False)
    ingredients = models.ManyToManyField(Ingredients)
    
    def __str__(self):
        return "%s" % (self.name)
    
    class Meta:
        verbose_name = _(u'Lista de la compra')
        verbose_name_plural = _(u'Listas de la compra')       
