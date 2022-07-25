from django.db import models


# Create your models here.
class Setai(models.Model):
    id = models.IntegerField(primary_key=True)
    sei = models.CharField(db_column='姓', max_length=32)

    class Meta:
        db_table = '世帯'


class Setaiin(models.Model):
    setai = models.ForeignKey(Setai, db_column='世帯ID', on_delete=models.PROTECT)
    mei = models.CharField(db_column='名前', max_length=32)

    class Meta:
        db_table = '世帯員'
