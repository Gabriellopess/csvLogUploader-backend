from django.urls import path
from csvFiles import views


app_name = 'csvFiles'

urlpatterns = [
    path('csvFiles/list', view=views.CsvFilesList.as_view(), name='csv-list'),
    path('csvFiles/rud/<int:pk>', view=views.CsvFilesRetrieveUpdateDestroy.as_view(), name='csv-rud'),
]