from . import serializers
from main import models
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


class HomeListSerializer(APIView):
    
    def get(self, request):
        serializer = serializers.HomeSerializer(models.Home.objects.order_by('-id').first())
        return Response(serializer.data)


class PortfolioListSerializer(generics.ListAPIView):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
   

class TeamMemberListSerializer(generics.ListAPIView):
    queryset = models.TeamMember.objects.all()
    serializer_class = serializers.TeamMemberSerializer
   

class VacancyListSerializer(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer
   

class VacancyDetailSerializer(APIView):

    def get(self, request, code):
        try:
            vacancy = models.Vacancy.objects.get(code=code)
            serializer = serializers.VacancySerializer(vacancy)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def message_create(request):
    try:
        models.Message.objects.create(
            name = request.data.get('name'),
            phone = request.data.get('phone'),
            body = request.data.get('body'),
        )
        return Response(status=status.HTTP_201_CREATED)
    except:
        print(222)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def resume_create(request):
    try:
        models.Resume.objects.create(
            full_name = request.data.get('full_name'),
            phone = request.data.get('phone'),
            resume = request.data.get('resume'),
        )
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    