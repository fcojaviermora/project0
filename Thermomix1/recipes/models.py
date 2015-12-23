#encoding:utf-8
'''
Created on 17 de nov. de 2015

@author: fjmora
'''
from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.fields.files import ImageField, FileField
from django.conf import settings
from __builtin__ import staticmethod
import datetime
from sorl.thumbnail import ImageField


# Unidades (Kg,g,l,etc.)
class Units(models.Model):    
    code = models.CharField(_(u'Código'),primary_key=True,max_length=10)
    description = models.CharField(_(u'Descripción'),max_length=100)
    
    def __str__(self):
        return "%s (%s)" % (self.code,self.description)
    
    class Meta:
        verbose_name = _(u'Unidad')
        verbose_name_plural = _(u'Unidades')        

# Categoría para materias
class Category(models.Model):
    code = CharField(_(u'Código'),max_length=10)             
    name = CharField(_(u'Nombre'),max_length=300)
    valid = models.BooleanField(_(u'Válido'),default=True)
    
    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')
        
        
# Materias primas
class Bom(models.Model):
    
    name = models.CharField(_(u'Nombre'),max_length=200)
    description = models.CharField(_(u'Descripción'),max_length=800)
    category = models.ForeignKey(Category,verbose_name=_(u'Categoría'))
    
    @staticmethod
    def autocomplete_search_fields():
        return ("name__iexact",)
    
    def __str__(self):
        return "%s" % (self.name)
    
    def __unicode__(self):
        return u"%s" % self.name
    
    def related_label(self):
        return u"%s" % (self.name)

    class Meta:
        verbose_name = _(u'Materia prima')
        verbose_name_plural = _(u'Materias primas')        

# Recetas
class Recipe(models.Model):    
    title = models.CharField(_(u'Título'),max_length=200)
    description = models.TextField(_(u'Descripción'),blank=True,null=True)    
    autor = models.CharField(_(u'Autor'),max_length=200,blank=True,null=True)
    is_thermomix = models.BooleanField(_(u'Thermomix'),default=True)
    saveBy = models.ForeignKey(User,verbose_name=_(u'Usuario'),blank=True,null=True)
    create_date = models.DateTimeField(_(u'Fecha de creación'))
    version = models.CharField(_(u'Versión'),max_length=100,default="1.0")       
    preparation = models.TextField(_(u'Preparación'))    
    aclaraciones = models.TextField(_(u'Aclaraciones'),blank=True,null=True)
    sugerencias = models.TextField(_(u'Sugerencias'),blank=True,null=True)    
    
    def __str__(self):
        return "%s" % (self.title)
    
    class Meta:
        verbose_name = _(u'Receta')
        verbose_name_plural = _(u'Recetas')
        

#Recetas favoritas de cada usuario
class UserFavoriteRecipe(models.Model):
    recipe = models.ForeignKey(Recipe,verbose_name=_(u'Receta'))
    user = models.ForeignKey(User,verbose_name=_(u'Usuario'))
    favorite = models.BooleanField(_(u'Favorita'),default=False)
    times = models.IntegerField(_(u'Veces realizada'),)

    class Meta:
        verbose_name = _(u'Recetas de usuario')
        verbose_name_plural = _(u'Recetas de usuario')       

class RecipeComment(models.Model):
    text = TextField()
    user = models.ForeignKey(User,verbose_name=_(u'Usuario'))
    recipe = models.ForeignKey(Recipe,verbose_name=_(u'Receta'))
    creation_date = models.DateTimeField()   
    
    class Meta:
        verbose_name = _(u'Comentario')
        verbose_name_plural = _(u'Comentarios') 

def content_file_name(instance, filename):
    return '/'.join(['recipe', instance.user.username, filename])

class RecipeImages(models.Model):
    profile_image = models.FileField(upload_to='recipes/%Y/%m/%d')    
    user = models.ForeignKey(User,verbose_name=_(u'Usuario'))
    recipe = models.ForeignKey(Recipe,verbose_name=_(u'Receta'))        
    
    class Meta:
        verbose_name = _(u'Imágenes de receta')
        verbose_name_plural = _(u'Imágenes de recetas')       

    
  
# Ingredientes, compuestos por una materia prima, cantidad, y unidada correspondiente
class Ingredients(models.Model):
    bom =  models.ForeignKey(Bom,verbose_name=_(u'Materias primas'))
    quantity = models.FloatField(_(u'Cantidad'),blank=True,null=True)
    units = models.ForeignKey(Units,blank=True,null=True,verbose_name=_(u'Unidades'))    
    recipe = models.ForeignKey(Recipe,verbose_name=_(u'Receta'))
    detalle = models.CharField(_(u'Detalle'),max_length=500,blank=True,null=True)
    
    def __str__(self):
        if self.quantity is not None and self.units is not None:
            return "%s - (%s %s)" % (self.bom.name, self.quantity,self.units.code)
        else:
            return "%s" % (self.bom.name)
     
    class Meta:
        verbose_name = _(u'Ingrediente')
        verbose_name_plural = _(u'Ingredientes')       
        
  
