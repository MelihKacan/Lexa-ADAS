from rest_framework import serializers
from .models import MainModel

class MainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainModel
        fields = ['id', 'value']
        extra_kwargs = {"id":{"read_only" :  True}}
    
    def create_data(self,validated_data):
        data1 = MainModel(
            value = validated_data["value"],
        )   
        data1.save()
        return data1