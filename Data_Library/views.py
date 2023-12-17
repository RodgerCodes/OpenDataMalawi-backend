from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from Data_Library.services import AddDataSetService, SearchDataSetService

from .models import Dataset, Field, FileFormat
from .serializer import DataSetSerializer, FieldSerializer, FileFormatSerializer


class GetFileFormat(generics.ListAPIView):
    """
    Get file formats
    """

    model = FileFormat
    serializer_class = FileFormatSerializer
    queryset = FileFormat.objects.all()


class GetFields(generics.ListAPIView):
    """
    Get datasets fields or categories
    """

    model = Field
    serializer_class = FieldSerializer
    queryset = Field.objects.all()


class AddDataSet(APIView):
    """
    View for adding dataset
    """

    serializer = DataSetSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        instance = AddDataSetService(request.data).add_dataset()
        return Response(instance, status=instance["status"])


class ViewDataSet(generics.RetrieveAPIView):
    """
    view for getting details of a single dataset
    """

    model = Dataset
    serializer_class = DataSetSerializer
    queryset = Dataset.objects.all()


class SearchDataSetsByName(APIView):
    """
    View for searching datasets by name
    """

    def get(self, request, searchQuery):
        instance = SearchDataSetService(searchQuery).searchDatasets()
        return Response(instance, status=instance["status"])


class FilterDataSetByField(APIView):
    """
    View for filtering datasets by field
    """

    def get(self, request, field):
        instance = SearchDataSetService(field).filterDatasets()
        return Response(instance, status=instance["status"])
