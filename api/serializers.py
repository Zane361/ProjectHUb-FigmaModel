from rest_framework import serializers
from main import models

class HomeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.Home
        exclude = ['id']


class PortfolioSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Portfolio
        exclude = ['id']


class TeamMemberSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.TeamMember
        exclude = ['id']


class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Message
        exclude = ['id']


class VacancySerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Vacancy
        exclude = ['id']


class ResumeSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Resume
        exclude = ['id']

