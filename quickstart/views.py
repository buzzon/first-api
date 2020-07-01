from quickstart.models import Snippet
from quickstart.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
