from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from  rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

from .models import Searching,FoundId,User
from .serializers import FoundIdSerializer,UserDetailsSerializer,SearchSerializer



@api_view()
def search(request,*args, **kwargs):
    print(request.GET.get('search'))
    search = get_object_or_404(FoundId,id_no = request.query_params['search'])
    serializer = FoundIdSerializer(search)
    return Response(serializer.data)


@permission_classes(AllowAny)
@authentication_classes([SessionAuthentication])
@api_view(['GET'])   
def getstats(request):
    collected = FoundId.objects.filter(picked=True).count()
    found = FoundId.objects.all().count()
    return Response({
        "Found": found,
        "collected": collected
        }) 

@api_view()
def get_recent(request):
    recent = FoundId.objects.all().order_by('-date_found')[:5]
    serializer = FoundIdSerializer(recent,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addid(request):
    user = request.user
    data = request.data
    data['station'] = user.station
    serializer = FoundIdSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class AddDetails(CreateAPIView):
    serializer_class = SearchSerializer
    queryset = Searching.objects.all()

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view()
def getuserdetails(request):
    user = request.user
    user_details = {
        "name": user.first_name,
        "station": user.station
    }
    
    return Response(user_details)


@api_view(['POST'])
def pick(request):
    user = request.user
    id_no = request.data['id_no']
    search = get_object_or_404(FoundId,id_no = id_no)
    search.picked = True
    search.save()
    return Response({"success":"success"})