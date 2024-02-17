from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from  rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import Searching,FoundId,User
from .serializers import FoundIdSerializer,UserDetailsSerializer,SearchSerializer


@api_view()
def home1(request):
    print(request.query_params['id'])
    return Response({"success":"succss"})


@api_view()
def search(request,*args, **kwargs):
    print(request.GET.get('search'))
    search = get_object_or_404(FoundId,id_no = request.query_params['search'])
    serializer = FoundIdSerializer(search)
    return Response(serializer.data)
 
@api_view()   
def getstats(request):
    collected = FoundId.objects.filter(picked=False).count()
    found = FoundId.objects.all().count()
    return Response({
        "Found": found,
        "collected": collected
        }) 

class AddId(CreateAPIView):
    serializer_class = FoundIdSerializer
    queryset = FoundId.objects.all()


class AddDetails(CreateAPIView):
    serializer_class = SearchSerializer
    queryset = Searching.objects.all()
