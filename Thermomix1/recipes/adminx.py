#encoding:utf-8
'''
Created on 17 de nov. de 2015

@author: fjmora
'''

from django.utils.safestring import mark_safe
import xadmin
from recipes.models import Ingredients, RecipeImages, Recipe, Category, Units,\
    UserFavoriteRecipe, Bom, RecipeComment
from xadmin.views.base import filter_hook
from django.utils.translation import ugettext as _
import datetime

class IngredientInlineAdmin(object):
    model = Ingredients
    extra = 0
    style = 'accordion'
    
class ImagesInlineAdmin(object):
    model = RecipeImages
    extra = 0
    style = 'tab' # other values: `one` (default), `table`, `accordian`
    

class IngredientsAdmin(object):
    fields = ('bom',)
    
     
class BomAdmin(object):
    list_display = ('name','description','category')
    list_editable = ('name', 'category')
    search_fields = ['name','description', 'category']
    list_filter = ['category']
    fields = ('name','description','category')
    

class RecipeAdmin(object):
    #TODO: En el formulario poner un check para identificarse uno mismo como el autor de la receta
    #inlines = [IngredientInlineAdmin,ImagesInlineAdmin]
    list_display = ('title','is_thermomix','version','create_date','view_recipe','favorite')
    list_editable = ('title','is_thermomix','version')
    exclude = ['create_date','saveBy']#,'saveBy'
    fieldsets = (
                 (None, {
                         'fields' : ('title','autor','version','preparation')
                         }),
                 )
    
    inlines = [IngredientInlineAdmin,ImagesInlineAdmin]
    
    #TODO: Pendiente de crear el html que muestre un resumen de la receta
    def view_recipe(self, obj):
        url = "<a href='/'><img src='/static/images/view.png'/></a>"
        return mark_safe(url)  
    
    #TODO: Pendiente de implementar la logica de favoritos
    def favorite(self, obj):
        url = "<a href='favorite_recipe/%s'><img src='/static/images/favorite_on.png'/></a>" % obj.id
        return mark_safe(url)  
    
    view_recipe.short_description = "Show recipe"
    view_recipe.is_column = True
    favorite.short_description = "Favorite"
    favorite.is_column = True    
        
    @filter_hook
    def save_models(self):
        self.new_obj.saveBy = self.user
        self.new_obj.create_date = datetime.datetime.now()
        self.new_obj.save()
#     @filter_hook
#     def save_forms(self):
#         self.form_obj.full_clean()     
#         item = self.org_obj or Recipe()
#         item.saveBy = self.request.user
#         
#         self.new_obj = item;    
#             
#         if self.form_obj.is_valid():
#             obj = self.form_obj.save(commit=False) # get just the object but don't commit it yet.
#             obj.save() # finally save it.
#             self.form_obj.save_m2m()
#       
#     @filter_hook
#     def save_related(self):
#         self.form_obj.save_m2m()    
        
class CategoryAdmin(object):
    pass

class UnitsAdmin(object):
    pass

class UserFavoriteRecipeAdmin(object):
    pass

class RecipeImageUserAdmin(object):
    list_display = ('recipe_image',)    
    
    def recipe_image(self, obj):
        url = u'<img src="/media/%s" style="height:100px;width:100px""/>' % obj.profile_image
        return url 
    
    recipe_image.allow_tags = True
    recipe_image.short_description = _(u'Imágenes')
  
    @filter_hook
    def save_models(self):
        self.new_obj.user = self.user        
        self.new_obj.save()

class RecipeCommentAdmin(object):
    exclude = ['user','creation_date']
    
    @filter_hook
    def save_models(self):
        self.new_obj.user = self.user
        self.new_obj.creation_date = datetime.datetime.now()
        self.new_obj.save()
    
#     fieldsets = (
#                  (None, {
#                          'fields' : ('text','recipe')
#                          }),
#                  )
    
   # exclude = ['user','creation_date']
    
#     @filter_hook
#     def save_forms(self):
#         self.form_obj.full_clean()     
#         item = self.org_obj or RecipeComment()
#         item.user = self.request.user
#         
#         self.new_obj = item;    
#             
#         if self.form_obj.is_valid():
#             obj = self.form_obj.save(commit=False) # get just the object but don't commit it yet.
#             obj.user = item.user
#             obj.save() # finally save it.
#             #self.form_obj.save_m2m()
#       
#     @filter_hook
#     def save_related(self):
#         pass   

xadmin.site.register(Recipe,RecipeAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Units,UnitsAdmin)
xadmin.site.register(Ingredients,IngredientsAdmin)
xadmin.site.register(UserFavoriteRecipe,UserFavoriteRecipeAdmin)
xadmin.site.register(RecipeImages,RecipeImageUserAdmin)
xadmin.site.register(Bom,BomAdmin)    
xadmin.site.register(RecipeComment,RecipeCommentAdmin)