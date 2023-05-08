from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.generics import DestroyAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from PIL import Image


class LCMyModelAPI(GenericAPIView, ListModelMixin, CreateModelMixin):  # list, create
   queryset = MyModel.objects.all()
   serializer_class = MyModelSerializer
   
   def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

   def post(self, request, *args, **kwargs):
      print(request.data['image_url'])
      img = Image.open(request.data['image_url'])
      max_colors = 1000
      print(img.getcolors(max_colors))
      kwargs['colors'] = img.getcolors(max_colors)
      return self.create(request, *args, **kwargs)

class RUDMyModelAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class MyModelViewSet(viewsets.ModelViewSet):
#   queryset = MyModel.objects.all()
#   serializer_class = MyModelSerializer
#   parser_classes = (MultiPartParser, FormParser)
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

