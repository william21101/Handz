from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from numpy import random

class User(AbstractUser):
    '''
    Custom User
    '''
    # hand_position = models.IntegerField(default=-1)
    is_logged_in = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Hand(object):
    def __init__(self, spades, hearts, diamonds, clubs):
        self.spades = spades
        self.hearts = hearts
        self.diamonds = diamonds
        self.clubs = clubs

def construct_hand(hand_int_list):

    spades, hearts, diamonds, clubs = '', '', '', ''

    def suit_rank(i):
        if i%13==0:
            return 'A'
        elif i%13==1:
            return 'K'
        elif i%13==10:
            return 'T'
        elif i%13==11:
            return 'Q'
        elif i%13==12:
            return 'J'
        else:
            return str(i%13)

    for x in hand_int_list:
        if x < 13:
            spades += suit_rank(x)
        elif x < 26:
            hearts += suit_rank(x)
        elif x < 39:
            diamonds += suit_rank(x)
        else:
            clubs += suit_rank(x)

    return Hand(spades,hearts,diamonds,clubs)

class Deal(object):

    def __init__(self, hand_string, north, south, east, west):
        self.hand_string = hand_string
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def direction(self, seat):
        if seat == 'north':
            return self.north
        elif seat == 'east':
            return self.east
        elif seat == 'south':
            return self.south
        elif seat == 'west':
            return self.west


def parse_deal(hand_string):

    north, south, east, west = [], [], [], []
    for i,x in enumerate(hand_string):
        if x =='N':
            north.append(i)
        elif x == 'S':
            south.append(i)
        elif x == 'E':
            east.append(i)
        elif x == 'W':
            west.append(i)

    deal = Deal(hand_string=hand_string,
            north=construct_hand(north),
            south=construct_hand(south),
            east=construct_hand(east),
            west=construct_hand(west))

    return deal

def construct_deal():
    l = list('NNNNNNNNNNNNNEEEEEEEEEEEEESSSSSSSSSSSSSWWWWWWWWWWWWW')
    random.shuffle(l)
    hand_string = ''.join(l)

    deal = parse_deal(hand_string)

    return deal


class DealField(models.Field):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 52
        super(DealField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(DealField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'deal'

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return parse_deal(value)

    def to_python(self, value):
        if isinstance(value, Deal):
            return value

        if value is None:
            return value

        return parse_deal(value)

    def get_prep_value(self, value):
        return value.hand_string

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': MyFormField}
        defaults.update(kwargs)
        return super(DealField, self).formfield(**defaults)

    def get_internal_type(self):
        return 'CharField'

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class BridgeTableManager(models.Manager):
    def create_deal(self):
        table = self.create(deal=construct_deal())
        return table

class BridgeTable(models.Model):
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    deal = DealField()
    objects = BridgeTableManager()
    # deal = models.ForeignKey(Deal, on_delete=models.CASCADE)



# class Deal(models.Model):
#     # bridge_table = models.ForeignKey(BridgeTable, on_delete=models.CASCADE)
#     deal_id = models.AutoField(primary_key=True, blank=True)
#     north = HandField()
#     south = HandField()
#     east = HandField()
#     west = HandField()
#
#     # dealer = models.IntegerField(default=1)
#     # vulnerability = models.IntegerField(default='')
#     # board_number = models.IntegerField(default=1)
#
#     hand_string = models.CharField(max_length=52)
#     objects = DealManager()
#     # in_play = models.BooleanField()
#     # next_player = models.IntegerField(default=-1)
