from django.urls import path
from csvFiles import views
from csvFiles import function_views


app_name = 'csvFiles'

urlpatterns = [
    path('csvFiles/list', view=views.CsvFilesList.as_view(), name='csv-list'),
    path('csvFiles/rud/<int:pk>', view=views.CsvFilesRetrieveUpdateDestroy.as_view(), name='csv-rud'),
    path('csv/upload', view=function_views.upload_csv, name='upload_csv'),
]