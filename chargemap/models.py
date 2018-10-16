from django.db import models

# Create your models here.

# Адреса
class Country (models.Model):
   country = models.CharField(max_length=100, null=True)
   def __str__(self):
       return self.country

class City (models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    city = models.CharField(max_length=100, null=True)
    def __str__(self):
        return '%s, %s' % (self.country, self.city)

# Оператор
class StationOperator (models.Model):
   operator = models.CharField(max_length=100, default=None)
   site = models.CharField(max_length=100, blank=True)
   def __str__(self):
       return self.operator

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
    charge_station_name = models.CharField(max_length=100, default='Зарядная станция')
    # Координаты 
    charge_station_latitude = models.FloatField(max_length=10, default=0)
    charge_station_longtitude = models.FloatField(max_length=10, default=0)
    # Тип зарядки
    charge_station_type = models.ForeignKey(ChargeStationType, on_delete=models.CASCADE, default=3)
    # Оператор (Моэск и пр)
    charge_station_operator = models.ForeignKey(StationOperator, on_delete=models.CASCADE, default=None)
    # Мощность, кВт
    charge_station_maxpower = models.IntegerField(default=0)
    # Тип разъема
    charge_station_plug = models.ManyToManyField(ChargeStationPlugType)
    # Статус: (свободна/забронирована/идет заправка)
    charge_station_status = models.ForeignKey(ChargeStationStatus, on_delete=models.CASCADE, default=3)
    # Оценка заправки (оценить удобство использования)
    charge_station_score = models.FloatField(default=0.0)
    # Рабочие часы (24/7, по рабочим дням и пр.)
    charge_station_working_time = models.ForeignKey(ChargeStationWorkingTime, on_delete=models.CASCADE, default=3)
    #Адрес заправки
    charge_station_city = models.ForeignKey(City, on_delete=models.CASCADE, default=1, null=True)
    charge_station_address = models.CharField(max_length=100, null=True)
    # Описание (пример: Находится на парковке ТЦ Globus, прямо у входа (дальний от Москвы). 
    # Доступ свободный. Открывается картой МОЭСК)
    charge_station_description = models.TextField(max_length=300, default='Станция зарядки электромобилей')
    

    def __str__(self):
        return '%s, %s' %(self.charge_station_name, self.charge_station_address)



#Фото заправки - не реализовано
#Стоимость заправки (тарифы) - не реализовано
#Способы оплаты (карта оператора, NFC, кредитная карта) - не реализовано
    