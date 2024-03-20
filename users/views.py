from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from .models import Searching,FoundId,User,Station
from .serializers import FoundIdSerializer,UserDetailsSerializer,SearchSerializer


@api_view()
def get_ids(request):
    station = request.user.station
    ids= FoundId.objects.filter(station=station)
    serializer = FoundIdSerializer(ids,many=True)
    return Response(serializer.data)


@api_view()
@permission_classes([AllowAny])
def search(request,*args, **kwargs):
    print(request.GET.get('search'))
    search = get_object_or_404(FoundId,id_no = request.query_params['search'])
    serializer = FoundIdSerializer(search)
    return Response(serializer.data)


@csrf_exempt   
@api_view(['GET'])
@permission_classes([AllowAny])
def getstats(request):
    # print(request.user.station)
    collected = FoundId.objects.filter(picked=True).count()
    not_picked = FoundId.objects.filter(picked=False).count()
    found = FoundId.objects.all().count()
    return Response({
        "Found": found,
        "collected": collected,
        "not_picked": not_picked
        })
 

@csrf_exempt   
@api_view(['GET'])
def getstats_by_station(request):
    print(request.user)
    collected = FoundId.objects.filter(station=request.user.station).filter(picked=True).count()
    not_picked = FoundId.objects.filter(station=request.user.station).filter(picked=True).count()
    found = FoundId.objects.filter(station=request.user.station).filter(picked=True).count()
    return Response({
        "Found": found,
        "collected": collected,
        "not_picked": not_picked
        }) 


@api_view()
@permission_classes([AllowAny])
def get_recent(request):
    recent = FoundId.objects.all().order_by('-date_found').filter(station=request.user.station)[:5]
    serializer = FoundIdSerializer(recent,many=True)
    print(serializer.data)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def addid(request):
    user = request.user
    station = request.user.station
    data = request.data
    try:
        id = FoundId.objects.get(id_no=data['id_no'])
        if id:
            id.picked = False
            id.station = user.station
            print(id.station.name)
            id.save()
            id_serializer = FoundIdSerializer(id)
            return Response(id_serializer.data,status=status.HTTP_201_CREATED)
    except FoundId.DoesNotExist:

        data['station'] = station
        print(data)
        serializer = FoundIdSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(station=station)
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
#  {
# "id_no":"9876543"
# }

class AddDetails(CreateAPIView):
    serializer_class = SearchSerializer
    queryset = Searching.objects.all()
    permission_classes = (AllowAny,)


@csrf_exempt
@api_view()
def getuserdetails(request):
    user = request.user
    user_details = {
        "name": user.first_name,
        "station": user.station.name
    }
    return Response(user_details)


@csrf_exempt
@api_view(['POST'])
def pick(request):
    id_no = request.data['id_no']
    search = get_object_or_404(FoundId,id_no = id_no)
    search.picked = True
    search.save()
    return Response({"success":"success"})
