from django.contrib.auth.models import User
from web_integration_app.models import Chain,Step
from web_integration_app.serializers import UserSerializer,ChainSerialiazer,StepSerializer
from rest_framework import viewsets
from rest_framework import permissions
from web_integration_app.permissions import IsOwnerOrReadOnly
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
import json
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChainViewSet(viewsets.ModelViewSet):
    queryset = Chain.objects.all()
    serializer_class = ChainSerialiazer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class FileUploadViewUPCS(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        lines = file_obj.readlines()
        for line in lines:
            ds = json.loads(line.decode('utf-8'))
            print("the data structure is : {}".format(ds))


        return Response(status=204)
