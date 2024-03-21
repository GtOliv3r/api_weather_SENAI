import datetime
from django.db import models
from django.core.exceptions import ValidationError

class WeatherEntity:

    def __init__(self, temperature, date,
                 city='', atmosphericPressure='',
                 humidity='', weather='') -> None:
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date

        # Validações
        if not isinstance(self.temperature, (int, float)):
            raise ValidationError("Temperature must be a number.")
        if not isinstance(self.date, datetime):
            raise ValidationError("Date must be a datetime object.")

    def __str__(self) -> str:
        return (f"Weather <{self.temperature}>")
