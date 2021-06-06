from django.contrib import admin
from django.urls import path , include
from proiectSI.views import WeatherListView
from . import views
app_name = 'proiectSI'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('weather/', include('proiectSI.urls'))
    path('', WeatherListView.as_view()),

]
