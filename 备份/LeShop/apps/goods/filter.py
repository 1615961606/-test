# coding: utf-8
__author__ = "wengwenyu"

import django_filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr="lte", help_text="最高价格")
    # 某个分类下的商品信息 （传进这个分类id） 自定义过滤器方法
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        # 去数据库里面 把查询出来的数据 进行过滤
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ('pricemin', "pricemax")
