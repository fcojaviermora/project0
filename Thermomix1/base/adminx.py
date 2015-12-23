'''
Created on 16 de dic. de 2015

@author: fjmora
'''
import xadmin
from xadmin import views


class MainDashboard(object):
    pass

xadmin.site.register(views.website.IndexView,MainDashboard)
    

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    
xadmin.site.register(views.BaseAdminView, BaseSetting)