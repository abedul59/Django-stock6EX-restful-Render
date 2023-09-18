from django.shortcuts import render
from rest_framework import viewsets, status
from images.models import Images, Stock6Sign202212, Stock6Sign202304, Stock6Sign202308
from images.serializers import ImageSerializer, Stock6Sign202212Serializer, Stock6Sign202304Serializer, Stock6Sign202308Serializer


# from ptt_beauty_images import settings
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models.aggregates import Count
from random import randint


# # single-databases
# def index_old(request):
#     return render(request, 'index.html', {
#         'images': Image.objects.values('id', 'Url').order_by('-CreateDate')
#     })


# # multiple-databases
# def index(request):
#     images_seq = []
#     for db_name in settings.DATABASES:
#         query = Image.objects.using(db_name).all()
#         for data in query:
#             dict_image = {
#                 'id': data.id,
#                 'Url': data.Url,
#                 'CreateDate': data.CreateDate
#             }
#             images_seq.append(dict_image)
#     images_seq = sorted(images_seq, key=lambda x: x['CreateDate'], reverse=True)
#     return render(request, 'index.html', {
#         'images': images_seq
#     })


# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Images.objects.all()
    serializer_class = ImageSerializer

    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="random")
    def get_random_image(self, request):
        count = Images.objects.aggregate(count=Count("id"))["count"]
        random_index = randint(0, count - 1)
        obj = Images.objects.all()[random_index]
        result = ImageSerializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)

class Stock6Sign202212ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202212.objects.all()
    serializer_class = Stock6Sign202212Serializer

    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo")
    def get_stock_info(self, request):

        obj = Stock6Sign202212.objects.all()
        result = Stock6Sign202212Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)

class Stock6Sign202304ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202304.objects.all()
    serializer_class = Stock6Sign202304Serializer

    # [ GET ] /api/image/random/
    #@action(detail=False, methods=["get"], url_path="getstockinfo")
    #def get_stock_info(self, request):

        #obj = Stock6Sign202304.objects.all()
        #result = Stock6Sign202304Serializer(obj)
        #return Response(result.data, status=status.HTTP_200_OK)
    
    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202304.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202304Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)
    

class Stock6Sign202308ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202308.objects.all()
    serializer_class = Stock6Sign202308Serializer


    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202308.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202308Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)
    

class Stock6Sign202309ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202309.objects.all()
    serializer_class = Stock6Sign202309Serializer


    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202309.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202309Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)
    
    
class Stock6Sign202310ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202310.objects.all()
    serializer_class = Stock6Sign202310Serializer


    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202310.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202310Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)
    

class Stock6Sign202311ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202311.objects.all()
    serializer_class = Stock6Sign202311Serializer


    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202311.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202311Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)


class Stock6Sign202312ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Stock6Sign202312.objects.all()
    serializer_class = Stock6Sign202312Serializer


    # [ GET ] /api/image/random/
    @action(detail=False, methods=["get"], url_path="getstockinfo/(?P<stockid_pk>[^/.]+)")
    def get_stock_info(self, request, stockid_pk, pk=None):

        obj = Stock6Sign202312.objects.get(cStockID=stockid_pk)
        result = Stock6Sign202312Serializer(obj)
        return Response(result.data, status=status.HTTP_200_OK)