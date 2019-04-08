from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters  # 过滤器
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend  # 导入我们自定义过滤器模块
from .serializers import GoodsSerializer, CategorySerializer, BannerSerializer
from .models import Goods, GoodsCategory, Banner
from .filter import GoodsFilter


class GoodsPagination(PageNumberPagination):
    """
      商品列表自定义分页
    """
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = "page"
    # 做多能显示多少页
    max_page_size = 100


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """商品后台逻辑"""
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief')
    ordering_fields = ('sold_num', "shop_price")


# ModelViewSet 增删改查
class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)  # 取出所有一级类目
    serializer_class = CategorySerializer  # 序列化使用的序列化类


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """首页轮播图"""
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
