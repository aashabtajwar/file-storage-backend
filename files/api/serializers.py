from rest_framework.serializers import Serializer, FileField


class FileSerializer(Serializer):
    file_upload = FileField()
    class Meta:
        fields = ['file']