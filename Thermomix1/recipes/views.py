from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from recipes.forms import RecipeImagesForm
from recipes.models import RecipeImages, Recipe, UserFavoriteRecipe
import mimetypes
from django.http.response import HttpResponse, HttpResponseRedirectBase

# Create your views here.

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = RecipeImagesForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = RecipeImages(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Thermomix.recipes.views.list'))
    else:
        form = RecipeImagesForm() # A empty, unbound form

    # Load documents for the list page
    documents = RecipeImages.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'recipes/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('recipes/index.html')


# View (in blog/views.py)
def change_favorite_recipe(request, id):
    recipe = Recipe.objects.filter(pk=id).first()
    favoriteRecipe = UserFavoriteRecipe.objects.filter(user__id=request.user.id,recipe__id=id).first()
    
    if favoriteRecipe is None:
        favoriteRecipe = UserFavoriteRecipe()
        favoriteRecipe.recipe = recipe
        favoriteRecipe.user = request.user
        favoriteRecipe.favorite = True
        favoriteRecipe.times = 0
    elif favoriteRecipe.favorite == False:        
        favoriteRecipe.favorite = True            
    else:
        favoriteRecipe.favorite = False        
    
    favoriteRecipe.save()  
    
        #return render(request, 'form.html', {'form': form})
    return render_to_response('../../')
    #return render_to_response('/recipes/recipe/model_list.html')
        
