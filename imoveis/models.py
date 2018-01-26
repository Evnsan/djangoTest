from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField

# Create your models here.

class Feature(models.Model):
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description

    class Meta:
        ordering = ["description"]

class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=True)
    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True, null=True)
    country_validator = RegexValidator(
        regex = r'^\+[\d\-\.]{1,6}$',
        message = "Um código de país pode ou não começar com um sinal de" +
                  "mais(+) e deve conter até 6 valores. Um valor pode ser um" +
                  "dígito(0-9), um ponto(.) ou um hífen(-)."
    )
    country =  models.CharField(
                   max_length=6,
                   validators=[country_validator],
                   blank=True,
                   default = '+55'
               )

    state_validator = RegexValidator(
        regex = r'\d{2,3}$',
        message = "Um código de região deve conter até 3 dígitos(0-9)."
    )
    state =  models.CharField(
                max_length=3,
                validators=[state_validator],
                default = '011'
                )

    number_validator = RegexValidator(
        regex = r'\d{8,9}$',
        message = "Um número de telefone deve conter de 8 a 9 dígitos(0-9)."
    )
    number = models.CharField(max_length=9, validators=[number_validator])
    def __str__(self):
        if self.country and self.state:
            return "+{} {} {}".format(self.country, self.state, self.number)
        elif self.state:
            return "{} {}".format(self.state, self.number)
        else:
            return str(self.number)

class PictureFile(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

class Picture(models.Model):
    title = models.CharField(max_length=200)
    picture_file = models.ImageField(
        upload_to='imoveis.PictureFile/bytes/filename/mimetype',
        blank = True,
        null = True)
    def __str__(self):
        return self.title[:20]

class Build(models.Model):
    pub_date = models.DateTimeField('data de cadastro')
    project = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    SELLING_CHOICES = ((True, 'à venda'), (False, 'vendido'))
    availability = models.BooleanField(choices=SELLING_CHOICES, default=True)
    age = models.PositiveIntegerField(default=0)
    building_type = models.CharField(max_length=200, blank=True)
    unit = models.PositiveIntegerField(default=0)
    tower = models.CharField(max_length=200, blank=True)
    FACE_CHOICES = (('N','Norte'), ('S', 'Sul'), ('L', 'Leste'),
                    ('O', 'Oeste'), ('-', 'Não informada'))
    face = models.CharField(max_length=1, choices=FACE_CHOICES, default='-')
    EMPTY_CHOICES = ((True, 'Sim'), (False, 'Não'))
    empty =  models.BooleanField(choices=EMPTY_CHOICES, default=True)
    selling_price = MoneyField(max_digits=15, decimal_places=2,
                             default_currency='BRL')
    iptu = MoneyField(max_digits=8, decimal_places=2,
                             default_currency='BRL')
    condominium_fee = MoneyField(max_digits=8, decimal_places=2,
                             default_currency='BRL')
    square_meters = models.PositiveIntegerField(default=0)
    units_per_floor = models.PositiveIntegerField(default=0, blank=True)
    janitor_name = models.CharField(max_length=200, blank=True)
    parking_slots = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    suites = models.PositiveIntegerField(default=0)
    features = models.ManyToManyField(Feature, blank=True)
    owners = models.ManyToManyField(Owner, blank=True)
    pictures = models.ManyToManyField(Picture, blank=True)

    class Meta:
        ordering = ["address"]

    def __str__(self):
        return self.address

class Observation(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.description[:10]
