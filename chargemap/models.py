from django.db import models

# Create your models here.

# Типы зарядки
class ChargeStationType (models.Model):
    station_type = models.CharField(max_length=100)
    # Схема разъема (картинка) - не реализовано
    def __str__(self):
        return self.station_type

# Типы разъемов
class ChargeStationPlugType (models.Model):
    plug_type = models.CharField(max_length=100)
    # Схема разъема (картинка) - не реализовано
    def __str__(self):
        return self.plug_type

# Статус зарядки
class ChargeStationStatus (models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status

# Рабочие часы зарядки
class ChargeStationWorkingTime (models.Model):
     working_time = models.CharField(max_length=100, default=None)
     def __str__(self):
        return self.working_time

# Описание зарядной станции
class ChargeStation (models.Model):
    # Наименование места (ТЦ ХХХ, Заправка Лукойл и пр.)
    charge_station_name = models.CharField(max_length=100)
    # Координаты 
    charge_station_latitude = models.FloatField(max_length=10, default=0)
    harge_station_longtitude = models.FloatField(max_length=10, default=0)
    # Тип зарядки
    charge_station_type = models.ForeignKey(ChargeStationType, on_delete=models.CASCADE, default=None)
    # Оператор (Моэск и пр)
    charge_station_operator = models.CharField(max_length=100)
    # Мощность, кВт
    charge_station_maxpower = models.IntegerField()
    # Тип разъема
    charge_station_plug = models.ManyToManyField(ChargeStationPlugType)
    # Статус: (свободна/забронирована/идет заправка)
    charge_station_status = models.ForeignKey(ChargeStationStatus, on_delete=models.CASCADE, default=None)
    # Оценка заправки (оценить удобство использования)
    charge_station_score = models.FloatField()
    # Рабочие часы (24/7, по рабочим дням и пр.)
    charge_station_working_time = models.ForeignKey(ChargeStationWorkingTime, on_delete=models.CASCADE, default=None)

    # Описание (пример: Находится на парковке ТЦ Globus, прямо у входа (дальний от Москвы). 
    # Доступ свободный. Открывается картой МОЭСК)
    charge_station_description = models.TextField(max_length=300)
    

    def __str__(self):
        return self.charge_station_name

# Адреса
class Address (models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)

#Фото заправки - не реализовано
#Стоимость заправки (тарифы) - не реализовано
#Способы оплаты (карта оператора, NFC, кредитная карта) - не реализовано
    