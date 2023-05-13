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

        model = Stock6Sign202304
        # fields = '__all__'
        fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate','RevN','Rev','a1N','a2N','a3N','a4N','a5N', 'a6N','a7N', 'na1','na2','na3','na4','na5','na6', 'na7','na9','na10','newest_Rev_month','luX','nluX_MoM','ProfitN','Profit','b1N','b2N','b3N','b4N','b5N','b6N','b7N','b8N','b1','b2','b3','b4','b5','b6', 'b7','b8','b9',  'b10','b10p','InvTON','InvTO','e1N','e2N','e3N','e4N','e5N','e6N','e7N','e8N','e1','e2','e3','e4','e5','e6','e7','e8','newest_Fin_Q','NetIncomeN','NetIncome','c1N','c2N','c3N','c4N','c5N','c6N', 'c7N','c8N','c1','c2','c3','c4','c5','c6','c7', 'c8', 'c9',  'c10','c11','pc9', 'pc10','pc11','EPSN','EPS','d1N','d2N','d3N','d4N','d5N','d6N','d7N','d8N','d1','d2','d3','d4','d5','d6','d7','d8','CashFlowN','CashFlow','f1N','f2N','f3N','f4N','f5N','f6N','f7N','f8N','f1','f2','f3','f4','f5','f6','f7','f8', 'f9','f10')

    