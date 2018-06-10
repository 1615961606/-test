from django.shortcuts import render
from .models import Banner, Post, BlogCategory, Comment, FriendlyLink, Tags
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class SearchView(View):
    def get(self, request):
        pass

    def post(self, request):
        # print(request.POST.get('keyword'))
        kw = request.POST.get('keyword')
        # post_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw)| Q(category__name__contains=kw))
        post_list = Post.objects.filter().all()
        ctx = {
            'post_list': post_list
        }
        return render(request, 'list.html', ctx)


# Create your views here.
def index(request):
    banner_list = Banner.objects.all()
    # 去数据库里面取出所有　推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    for recoment in recomment_list:
        recoment.content = recoment.content[:100] + '......'

    # 取出所有文章　按照时间倒序
    post_list = Post.objects.order_by('-pub_date')
    for post in post_list:
        post.content = post.content[:160] + '......'

    # 博客分类
    blogcategory_list = BlogCategory.objects.all()

    # 最新评论博客列表
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            new_comment_list.append(test.post)
    # # 空的博客列表
    # new_comment_list = []
    # # 临时的id列表
    # test_id_list = []
    # for test in comment_list:
    #     if test.post.id not in test_id_list:
    #         test_id_list.append(test.post.id)
    #         new_comment_list.append(test.post)
    # 友情链接
    friendlylink_list = FriendlyLink.objects.all()

    # 分页

    try:
        page = request.GET.get('page', 1)
    except:
        page = 1

    p = Paginator(post_list, per_page=2, request=request)
    post_list = p.page(page)

    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list,
        'friendlylink_list': friendlylink_list

    }
    return render(request, 'index.html', ctx)


def blog_list(request, tid=-1):
    # tid=-1时候 代表的是  从列表过来
    tid = int(tid)
    post_list = None
    if tid != -1:
        post_list = Post.objects.filter(tags=tid)
    else:
        post_list = Post.objects.order_by('-pub_date')

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, per_page=10, request=request)
    post_list = p.page(page)

    # 取出所有标签
    tags = Tags.objects.all()
    tag_message_list = []

    for t in tags:
        count = len(t.post_set.all())
        tag_message_list.append({'name': t.name, 'id': t.id, 'count': count})

    ctx = {
        'post_list': post_list,
        'tag_message_list': tag_message_list
    }

    return render(request, 'list.html', ctx)