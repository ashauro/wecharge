from django.db import models

# Create your models here.

# Типы разъемов
class ChargeStationPlugType (models.Model):
    plug_type_1 = models.CharField(max_length=100)
    plug_type_2 = models.CharField(max_length=100)
    # Схема разъема (картинка) - не реализовано

# Когда доступна (24/7, по рабочим дням и пр.)
class ChargeStationAvailability (models.Model):
    charge_station_available = models.CharField(default='No data', max_length=100)
    charge_station_not_available = models.CharField(default='No data', max_length=100)
    charge_station_not_data = models.CharField(default='No data', max_length=100)

# Описание зарядной станции
class ChargeStation (models.Model):
    # Наименование места (ТЦ ХХХ, Заправка Лукойл и пр.)
    charge_station_name = models.CharField(max_length=100)
    # Оператор (Моэск и пр)
    charge_station_operator = models.CharField(max_length=100)
    # Мощность, кВт
    charge_station_maxpower = models.IntegerField()
    # Тип разъема
    charge_station_plug = models.ForeignKey(ChargeStationPlugType, default='0', on_delete=models.CASCADE)
    # Статус: (свободна/забронирована/идет заправка)
    charge_station_status = models.ForeignKey(ChargeStationAvailability, default='0', on_delete=models.CASCADE)
    # Оценка заправки (оценить удобство использования)
    charge_station_score = models.FloatField()
    # Когда доступна (24/7, по рабочим дням и пр.)
    # Описание (пример: Находится на парковке ТЦ Globus, прямо у входа (дальний от Москвы). 
    # Доступ свободный. Открывается картой МОЭСК)
    charge_station_description = models.TextField(max_length=200)

    def __str__(self):
        return self.charge_station_name

# Адреса
class Address (models.Model):
    charge_station = models.ForeignKey(ChargeStation, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)

#Фото заправки - не реализовано
#Стоимость заправки (тарифы) - не реализовано
#Способы оплаты (карта оператора, NFC, кредитная карта) - не реализовано
    