from django.db import models


# Create your models here.
class Images(models.Model):
    Url = models.TextField()
    CreateDate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'Images'
    def __str__(self):
        return self.Url
    
class Stock6Sign202212(models.Model):
    #Url = models.TextField()
    
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    
    CreateDate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'Stock6Sign202212'
    def __str__(self):
        return self.cStockID

class Stock6Sign202304(models.Model):
    #Url = models.TextField()
    
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    
    CreateDate = models.DateTimeField()

        #營收屬性
    cRevN = models.CharField(max_length=100)
    cRev = models.CharField(max_length=100)
    ca1N = models.CharField(max_length=10)
    ca2N = models.CharField(max_length=10)
    ca3N = models.CharField(max_length=10)
    ca4N = models.CharField(max_length=10)
    ca5N = models.CharField(max_length=10) 
    ca6N = models.CharField(max_length=10)        
    ca7N = models.CharField(max_length=10)

    cna1 = models.CharField(max_length=10)
    cna2 = models.CharField(max_length=10)
    cna3 = models.CharField(max_length=10)
    cna4 = models.CharField(max_length=10)
    cna5 = models.CharField(max_length=10)
    cna6 = models.CharField(max_length=10) 
    cna7 = models.CharField(max_length=10)
    cna9 = models.CharField(max_length=10)
    cna10 = models.CharField(max_length=10)
    cnewest_Rev_month = models.CharField(max_length=10)
    cluX = models.CharField(max_length=10)
    cnluX_MoM = models.CharField(max_length=10)

        #2 and 5
    cProfitN = models.CharField(max_length=100)
    cProfit = models.CharField(max_length=100)
    cb1N = models.CharField(max_length=10)
    cb2N = models.CharField(max_length=10)
    cb3N = models.CharField(max_length=10)
    cb4N = models.CharField(max_length=10)
    cb5N = models.CharField(max_length=10)
    cb6N = models.CharField(max_length=10)       
    cb7N = models.CharField(max_length=10)
    cb8N = models.CharField(max_length=10)

    cb1 = models.CharField(max_length=10)
    cb2 = models.CharField(max_length=10)
    cb3 = models.CharField(max_length=10)
    cb4 = models.CharField(max_length=10)
    cb5 = models.CharField(max_length=10)
    cb6 = models.CharField(max_length=10) 
    cb7 = models.CharField(max_length=10)
    cb8 = models.CharField(max_length=10)
    cb9 = models.CharField(max_length=10)  
    cb10 = models.CharField(max_length=10)
    cb10p = models.CharField(max_length=10)
    cInvTON = models.CharField(max_length=100)
    cInvTO= models.CharField(max_length=100)
    ce1N = models.CharField(max_length=10)
    ce2N = models.CharField(max_length=10)
    ce3N = models.CharField(max_length=10)
    ce4N = models.CharField(max_length=10)
    ce5N = models.CharField(max_length=10)
    ce6N = models.CharField(max_length=10)
    ce7N = models.CharField(max_length=10)
    ce8N = models.CharField(max_length=10)
    ce1 = models.CharField(max_length=10)
    ce2 = models.CharField(max_length=10)
    ce3 = models.CharField(max_length=10)
    ce4 = models.CharField(max_length=10)
    ce5 = models.CharField(max_length=10)
    ce6 = models.CharField(max_length=10)
    ce7 = models.CharField(max_length=10)
    ce8 = models.CharField(max_length=10)
    cnewest_Fin_Q = models.CharField(max_length=10)
        
       #  stock_NetInc3_EPS4(stock_id)
        #3 and 4
    cNetIncomeN = models.CharField(max_length=100)
    cNetIncome = models.CharField(max_length=100)
    cc1N = models.CharField(max_length=10)
    cc2N = models.CharField(max_length=10)
    cc3N = models.CharField(max_length=10)
    cc4N = models.CharField(max_length=10)
    cc5N = models.CharField(max_length=10)
    cc6N = models.CharField(max_length=10)      
    cc7N = models.CharField(max_length=10)
    cc8N = models.CharField(max_length=10)
    cc1 = models.CharField(max_length=10)
    cc2 = models.CharField(max_length=10)
    cc3 = models.CharField(max_length=10)
    cc4 = models.CharField(max_length=10)
    cc5 = models.CharField(max_length=10)
    cc6 = models.CharField(max_length=10)        
    cc7 = models.CharField(max_length=10) 
    cc8 = models.CharField(max_length=10) 
    cc9 = models.CharField(max_length=10)  
    cc10 = models.CharField(max_length=10)
    cc11 = models.CharField(max_length=10)
    cpc9 = models.CharField(max_length=10) 
    cpc10 = models.CharField(max_length=10)
    cpc11 = models.CharField(max_length=10)

    cEPSN = models.CharField(max_length=100)
    cEPS= models.CharField(max_length=100)
    cd1N = models.CharField(max_length=10)
    cd2N = models.CharField(max_length=10)
    cd3N = models.CharField(max_length=10)
    cd4N = models.CharField(max_length=10)
    cd5N = models.CharField(max_length=10)
    cd6N = models.CharField(max_length=10)
    cd7N = models.CharField(max_length=10)
    cd8N = models.CharField(max_length=10)
    cd1 = models.CharField(max_length=10)
    cd2 = models.CharField(max_length=10)
    cd3 = models.CharField(max_length=10)
    cd4 = models.CharField(max_length=10)
    cd5 = models.CharField(max_length=10)
    cd6 = models.CharField(max_length=10)
    cd7 = models.CharField(max_length=10)
    cd8 = models.CharField(max_length=10)
       #
       #= stock_Cashflow6(stock_id)
        #6
    cCashFlowN = models.CharField(max_length=100)
    cCashFlow = models.CharField(max_length=100)
    cf1N = models.CharField(max_length=10)
    cf2N = models.CharField(max_length=10)
    cf3N = models.CharField(max_length=10)
    cf4N = models.CharField(max_length=10)
    cf5N = models.CharField(max_length=10)
    cf6N = models.CharField(max_length=10)       
    cf7N = models.CharField(max_length=10)
    cf8N = models.CharField(max_length=10)
    cf1 = models.CharField(max_length=10)
    cf2 = models.CharField(max_length=10)
    cf3 = models.CharField(max_length=10)
    cf4 = models.CharField(max_length=10)
    cf5 = models.CharField(max_length=10)
    cf6 = models.CharField(max_length=10)        
    cf7 = models.CharField(max_length=10)
    cf8 = models.CharField(max_length=10) 
    cf9 = models.CharField(max_length=10)  
    cf10 = models.CharField(max_length=10)




    class Meta:
        # managed = False
        db_table = 'Stock6Sign202304'
    def __str__(self):
        return self.cStockID    

class Stock6Sign202308(models.Model):
    #Url = models.TextField()
    
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    
    CreateDate = models.DateTimeField()

        #營收屬性
    cRevN = models.CharField(max_length=100)
    cRev = models.CharField(max_length=100)
    ca1N = models.CharField(max_length=10)
    ca2N = models.CharField(max_length=10)
    ca3N = models.CharField(max_length=10)
    ca4N = models.CharField(max_length=10)
    ca5N = models.CharField(max_length=10) 
    ca6N = models.CharField(max_length=10)        
    ca7N = models.CharField(max_length=10)

    cna1 = models.CharField(max_length=10)
    cna2 = models.CharField(max_length=10)
    cna3 = models.CharField(max_length=10)
    cna4 = models.CharField(max_length=10)
    cna5 = models.CharField(max_length=10)
    cna6 = models.CharField(max_length=10) 
    cna7 = models.CharField(max_length=10)
    cna9 = models.CharField(max_length=10)
    cna10 = models.CharField(max_length=10)
    cnewest_Rev_month = models.CharField(max_length=10)
    cluX = models.CharField(max_length=10)
    cnluX_MoM = models.CharField(max_length=10)

        #2 and 5
    cProfitN = models.CharField(max_length=100)
    cProfit = models.CharField(max_length=100)
    cb1N = models.CharField(max_length=10)
    cb2N = models.CharField(max_length=10)
    cb3N = models.CharField(max_length=10)
    cb4N = models.CharField(max_length=10)
    cb5N = models.CharField(max_length=10)
    cb6N = models.CharField(max_length=10)       
    cb7N = models.CharField(max_length=10)
    cb8N = models.CharField(max_length=10)

    cb1 = models.CharField(max_length=10)
    cb2 = models.CharField(max_length=10)
    cb3 = models.CharField(max_length=10)
    cb4 = models.CharField(max_length=10)
    cb5 = models.CharField(max_length=10)
    cb6 = models.CharField(max_length=10) 
    cb7 = models.CharField(max_length=10)
    cb8 = models.CharField(max_length=10)
    cb9 = models.CharField(max_length=10)  
    cb10 = models.CharField(max_length=10)
    cb10p = models.CharField(max_length=10)
    cInvTON = models.CharField(max_length=100)
    cInvTO= models.CharField(max_length=100)
    ce1N = models.CharField(max_length=10)
    ce2N = models.CharField(max_length=10)
    ce3N = models.CharField(max_length=10)
    ce4N = models.CharField(max_length=10)
    ce5N = models.CharField(max_length=10)
    ce6N = models.CharField(max_length=10)
    ce7N = models.CharField(max_length=10)
    ce8N = models.CharField(max_length=10)
    ce1 = models.CharField(max_length=10)
    ce2 = models.CharField(max_length=10)
    ce3 = models.CharField(max_length=10)
    ce4 = models.CharField(max_length=10)
    ce5 = models.CharField(max_length=10)
    ce6 = models.CharField(max_length=10)
    ce7 = models.CharField(max_length=10)
    ce8 = models.CharField(max_length=10)
    cnewest_Fin_Q = models.CharField(max_length=10)
        
       #  stock_NetInc3_EPS4(stock_id)
        #3 and 4
    cNetIncomeN = models.CharField(max_length=100)
    cNetIncome = models.CharField(max_length=100)
    cc1N = models.CharField(max_length=10)
    cc2N = models.CharField(max_length=10)
    cc3N = models.CharField(max_length=10)
    cc4N = models.CharField(max_length=10)
    cc5N = models.CharField(max_length=10)
    cc6N = models.CharField(max_length=10)      
    cc7N = models.CharField(max_length=10)
    cc8N = models.CharField(max_length=10)
    cc1 = models.CharField(max_length=10)
    cc2 = models.CharField(max_length=10)
    cc3 = models.CharField(max_length=10)
    cc4 = models.CharField(max_length=10)
    cc5 = models.CharField(max_length=10)
    cc6 = models.CharField(max_length=10)        
    cc7 = models.CharField(max_length=10) 
    cc8 = models.CharField(max_length=10) 
    cc9 = models.CharField(max_length=10)  
    cc10 = models.CharField(max_length=10)
    cc11 = models.CharField(max_length=10)
    cpc9 = models.CharField(max_length=10) 
    cpc10 = models.CharField(max_length=10)
    cpc11 = models.CharField(max_length=10)

    cEPSN = models.CharField(max_length=100)
    cEPS= models.CharField(max_length=100)
    cd1N = models.CharField(max_length=10)
    cd2N = models.CharField(max_length=10)
    cd3N = models.CharField(max_length=10)
    cd4N = models.CharField(max_length=10)
    cd5N = models.CharField(max_length=10)
    cd6N = models.CharField(max_length=10)
    cd7N = models.CharField(max_length=10)
    cd8N = models.CharField(max_length=10)
    cd1 = models.CharField(max_length=10)
    cd2 = models.CharField(max_length=10)
    cd3 = models.CharField(max_length=10)
    cd4 = models.CharField(max_length=10)
    cd5 = models.CharField(max_length=10)
    cd6 = models.CharField(max_length=10)
    cd7 = models.CharField(max_length=10)
    cd8 = models.CharField(max_length=10)
       #
       #= stock_Cashflow6(stock_id)
        #6
    cCashFlowN = models.CharField(max_length=100)
    cCashFlow = models.CharField(max_length=100)
    cf1N = models.CharField(max_length=10)
    cf2N = models.CharField(max_length=10)
    cf3N = models.CharField(max_length=10)
    cf4N = models.CharField(max_length=10)
    cf5N = models.CharField(max_length=10)
    cf6N = models.CharField(max_length=10)       
    cf7N = models.CharField(max_length=10)
    cf8N = models.CharField(max_length=10)
    cf1 = models.CharField(max_length=10)
    cf2 = models.CharField(max_length=10)
    cf3 = models.CharField(max_length=10)
    cf4 = models.CharField(max_length=10)
    cf5 = models.CharField(max_length=10)
    cf6 = models.CharField(max_length=10)        
    cf7 = models.CharField(max_length=10)
    cf8 = models.CharField(max_length=10) 
    cf9 = models.CharField(max_length=10)  
    cf10 = models.CharField(max_length=10)




    class Meta:
        # managed = False
        db_table = 'Stock6Sign202308'
    def __str__(self):
        return self.cStockID 