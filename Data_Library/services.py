from abc import ABC, abstractmethod
from rest_framework import status
from Data_Library.models import Field, FileFormat
from Data_Library.serializer import DataSetSerializer


class IDataSetAbstractMethod(ABC):
    @abstractmethod
    def get_fileType(self, fileTypeID):
        pass

    @abstractmethod
    def get_field_of_usage(self, fieldID):
        pass


class AddDataSetService(IDataSetAbstractMethod):
    """
    Service for adding datasets in the system
    """

    serializer = DataSetSerializer

    def __init__(self, request_data):
        self.request_data = request_data

    def get_fileType(self, fileTypeID):
        try:
            return FileFormat.objects.get(id=fileTypeID)
        except FileFormat.DoesNotExist:
            return None

    def get_field_of_usage(self, fieldID):
        try:
            return Field.objects.get(id=fieldID)
        except Field.DoesNotExist:
            return None

    def _save_dataset(self):
        dataSerializer = self.serializer(self.request_data)
        dataSerializer.is_valid(raise_exception=True)
        return dataSerializer

    def add_dataset(self) -> dict:
        fileTypeInstance = self.get_fileType(self.request_data["fileType"])

        if fileTypeInstance is None:
            return {
                "message": "File Type does not exits",
                "status": status.HTTP_404_NOT_FOUND,
            }

        fieldInstance = self.get_field_of_usage(self.request_data["field"])

        if fieldInstance is None:
            return {
                "message": "Field Does not Exists",
                "status": status.HTTP_404_NOT_FOUND,
            }
        self._save_dataset()
        return {"message": "Dateset successfully added", "status": status.HTTP_200_OK}
