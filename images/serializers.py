from rest_framework import serializers

from images.models import Images
from images.models import Stock6Sign202212, Stock6Sign202304


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        # fields = '__all__'
        fields = ('id', 'Url', 'CreateDate')
        
class Stock6Sign202212Serializer(serializers.ModelSerializer):
    class Meta:

        model = Stock6Sign202212
        # fields = '__all__'
        fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate')

class Stock6Sign202304Serializer(serializers.ModelSerializer):
    class Meta:
        #name = serializers.CharField(required=False) # Maybe add read_only or write_only
        model = Stock6Sign202304
        # fields = '__all__'
        fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate', 'cRevN', 'cRev','ca1N','ca2N','ca3N','ca4N','ca5N', 'ca6N','ca7N', 'cna1','cna2','cna3','cna4','cna5','cna6', 'cna7','cna9','cna10','cnewest_Rev_month','cluX','cnluX_MoM','cProfitN','cProfit','cb1N','cb2N','cb3N','cb4N','cb5N','cb6N','cb7N','cb8N','cb1','cb2','cb3','cb4','cb5','cb6', 'cb7','cb8','cb9',  'cb10','cb10p','cInvTON','cInvTO','ce1N','ce2N','ce3N','ce4N','ce5N','ce6N','ce7N','ce8N','ce1','ce2','ce3','ce4','ce5','ce6','ce7','ce8','cnewest_Fin_Q','cNetIncomeN','cNetIncome','cc1N','cc2N','cc3N','cc4N','cc5N','cc6N', 'cc7N','cc8N','cc1','cc2','cc3','cc4','cc5','cc6','cc7', 'cc8', 'cc9',  'cc10','cc11','cpc9', 'cpc10','cpc11','cEPSN','cEPS','cd1N','cd2N','cd3N','cd4N','cd5N','cd6N','cd7N','cd8N','cd1','cd2','dc3','cd4','cd5','cd6','cd7','cd8','cCashFlowN','cCashFlow','cf1N','cf2N','cf3N','cf4N','cf5N','cf6N','cf7N','cf8N','cf1','cf2','cf3','cf4','cf5','cf6','cf7','cf8', 'cf9','cf10')

    