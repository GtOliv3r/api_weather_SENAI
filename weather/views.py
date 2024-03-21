from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherEntitySerializer

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        serializer = WeatherEntitySerializer(data=weathers, many=True)
        serializer.is_valid()
        serialized_data = serializer.data
        return render(request, "home.html", {"weathers": serialized_data})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')

        # Gerar dados aleatórios
        data = {
            "city": "Sorocaba",
            "temperature": randrange(start=17, stop=40),
            "date": datetime.now(),
            "humidity": randrange(start=20, stop=30),
            "weather": randrange(start=20, stop=23),
            "atmosphericPressure": randrange(start=1008, stop=1010),
        }

        # Serializar os dados
        serializer = WeatherEntitySerializer(data=data)

        # Validar os dados
        if serializer.is_valid():
            # Se os dados forem válidos, inseri-los no banco de dados
            repository.insert(serializer.validated_data)
        else:
            # Se os dados forem inválidos, lidar com os erros (neste caso, apenas imprimir os erros)
            print(serializer.errors)

        return redirect('Weather View')

    
class WeatherReset(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()
        return redirect('Weather View')
