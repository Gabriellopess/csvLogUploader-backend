from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .models import CsvFiles    
from .serializer import CsvFilesSerializer
from rest_framework import status

@api_view(('GET', 'PUT', ))
@authentication_classes([])
@permission_classes([])
def upload_csv(request):
    if request.method == 'GET':
        csv = CsvFiles.objects.all()
        serializer =CsvFilesSerializer(csv, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        csv_file = request.FILES.get('file')
        nome = request._full_data['fileName']
        dict = {'nome': nome,'csv': csv_file}
        serializer = CsvFilesSerializer(data=dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
