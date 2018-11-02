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
     time = models.CharField(max_length=100, default=None)
     def __str__(self):
        return self.time

# Описание зарядной станции
class ChargeStation (models.Model):
    # Наименование места (ТЦ ХХХ, Заправка Лукойл и пр.)
    name = models.CharField(max_length=100, default='Зарядная станция')
    # Координаты 
    latitude = models.FloatField(max_length=10, default=0)
    longtitude = models.FloatField(max_length=10, default=0)
    # Тип зарядки
    station_type = models.ForeignKey(ChargeStationType, on_delete=models.CASCADE, default=3)
    # Оператор (Моэск и пр)
    operator = models.ForeignKey(StationOperator, on_delete=models.CASCADE, default=None)
    # Модель станции
    station_model = models.CharField(max_length=100, null=True)
    # Мощность, кВт
    maxpower = models.IntegerField(default=0)
    # Тип разъема
    plug = models.ManyToManyField(ChargeStationPlugType)
    # Статус: (свободна/забронирована/идет заправка)
    status = models.ForeignKey(ChargeStationStatus, on_delete=models.CASCADE, default=3)
    # Оценка заправки (оценить удобство использования)
    score = models.FloatField(default=0.0)
    # Рабочие часы (24/7, по рабочим дням и пр.)
    working_time = models.ForeignKey(ChargeStationWorkingTime, on_delete=models.CASCADE, default=3)
    #Адрес заправки
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1, null=True)
    address = models.CharField(max_length=100, null=True)
    # Описание (пример: Находится на парковке ТЦ Globus, прямо у входа (дальний от Москвы). 
    # Доступ свободный. Открывается картой МОЭСК)
    description = models.TextField(max_length=300, default='Станция зарядки электромобилей')
    

    def __str__(self):
        return '%s, %s' %(self.name, self.address)



#Фото заправки - не реализовано
#Стоимость заправки (тарифы) - не реализовано
#Способы оплаты (карта оператора, NFC, кредитная карта) - не реализовано
    