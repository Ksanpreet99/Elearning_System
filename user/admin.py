from django.contrib import admin
from .models import Courses
from .models import Tutorialmodel
from .models import QuesModel
from admin_interface.models import Theme
from django.contrib.auth.models import Group

# Register your models here
admin.site.site_header='E-Learn Admin Dashboard'
admin.site.site_title = 'E-Learn Dashboard'
admin.site.index_title = 'Welcome to E-Learning.....'

admin.site.register(Courses)
admin.site.register(Tutorialmodel)
admin.site.register(QuesModel)
#admin.site.unregister(Theme)