from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator

from .models import NTT, NNTName, CityName, Streets, Blog, Grant, NormativHujjat, OAV, Index, TextModel


def index(request):
    index = Index.objects.first()
    text_data = TextModel.objects.all()
    language_code = request.LANGUAGE_CODE

    return render(request, 'index.html', {'index': index, 'language_code': language_code, 'data': text_data})


def blog(request):
    index = Index.objects.first()  # Retrieve the first Index object or None
    last_blog = Blog.objects.latest('id')
    query = request.GET.get('q')
    language_code = request.LANGUAGE_CODE

    if query:
        blog = Blog.objects.filter(title__icontains=query).order_by('-id')
    else:
        blog = Blog.objects.all().order_by('-id')

    paginator = Paginator(blog, 5)  # 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blog': page_obj,
        'last_blog': last_blog,
        'index': index,  # Pass the first Index object
        'language_code': language_code  # Pass the current language code
    }
    return render(request, 'blog.html', context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogChild.html'  # Shablon nomi
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index = Index.objects.first()
        language_code = self.request.LANGUAGE_CODE
        # Boshqa modeldan malumotlarni olish
        recent_post = Blog.objects.all()
        context['recent_post'] = recent_post
        context['index'] = index
        context['language_code'] = language_code
        return context


def grant(request):
    query = request.GET.get('q')  # Foydalanuvchi tomonidan kiritilgan so'rovi olish
    last_grant = Grant.objects.all().order_by('id')
    index = Index.objects.first()
    language_code = request.LANGUAGE_CODE

    # Agar so'rov mavjud bo'lsa, Grant obyektlarini filtratsiya qilish
    if query:
        grant = Grant.objects.filter(title__icontains=query).order_by('-id')
    else:
        # Aks holda, barcha Grant obyektlarini olish
        grant = Grant.objects.all().order_by('-id')

    paginator = Paginator(grant, 5)  # Har bir sahifada 5 ta grant
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'grant': grant,
        'last_grant': last_grant,
        'grant': page_obj,
        'index': index,
        'language_code': language_code,
    }
    return render(request, 'grant.html', context)


class GrantDetailView(DetailView):
    model = Grant
    template_name = 'grantdetail.html'  # Shablon nomi
    context_object_name = 'grant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index = Index.objects.first()
        language_code = self.request.LANGUAGE_CODE
        # Boshqa modeldan malumotlarni olish
        recent_grant = Grant.objects.all()
        context['recent_grant'] = recent_grant
        context['index'] = index
        context['language_code'] = language_code
        return context


def oav(request):
    index = Index.objects.first()
    language_code = request.LANGUAGE_CODE
    tv = OAV.objects.filter(choice_field='TV')
    gazeta = OAV.objects.filter(choice_field='Gazeta')
    jurnal = OAV.objects.filter(choice_field='Jurnal')

    paginator = Paginator(gazeta, 5)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tv': tv,
        'gazeta': page_obj,
        'jurnal': jurnal,
        'index': index,
        'language_code': language_code,
    }
    return render(request, 'oav.html', context)


class OAVDetailView(DetailView):
    model = OAV
    template_name = 'oavdetail.html'  # Shablon nomi
    context_object_name = 'oav'

    def get_context_data(self, **kwargs):
        index = Index.objects.first()
        language_code = self.request.LANGUAGE_CODE
        context = super().get_context_data(**kwargs)
        # Boshqa modeldan malumotlarni olish
        context['index'] = index
        context['language_code'] = language_code

        return context


# def nnt(request):
#     nnt_name = NNTName.objects.all()
#     nnt_id = request.GET.get('nnt_name')
#     if nnt_id:
#         nnt = NTT.objects.filter(nnt=nnt_id)
#     else:
#         nnt = NTT.objects.filter(name='nom 1')
#
#     paginator = Paginator(nnt_name, 2)  # Har bir sahifada 5 ta grant
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'nnt_name': page_obj,
#         'nnt': nnt
#     }
#     return render(request, 'nnt.html', context)
#


def nnt(request):
    index = Index.objects.first()
    language_code = request.LANGUAGE_CODE

    nnt_name = NNTName.objects.all()
    nnt_id = request.GET.get('nnt_name')
    search_query = request.GET.get('q')  # Bu qatorni qo'shing

    if nnt_id:
        nnt = NTT.objects.filter(nnt=nnt_id)
    else:
        if search_query:  # Agar qidiruv so'rov mavjud bo'lsa
            nnt = NTT.objects.filter(
                Q(name__icontains=search_query) | Q(director__icontains=search_query))  # Ma'lumotlarni qidirish
        else:
            nnt = NTT.objects.filter(name='nom 1')

    paginator = Paginator(nnt_name, 10)  # Har bir sahifada 5 ta grant
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'nnt_name': page_obj,
        'nnt': nnt,
        'index': index,
        'language_code': language_code
    }
    return render(request, 'nnt.html', context)


def streets(request):
    index = Index.objects.first()
    language_code = request.LANGUAGE_CODE
    city = CityName.objects.all()
    street_name = request.GET.get('q')

    if street_name:
        street = Streets.objects.filter(city__name__icontains=street_name)
    else:
        street_id = request.GET.get('city')
        if street_id:
            street = Streets.objects.filter(city=street_id)
        else:
            street = None

    paginator = Paginator(city, 10)  # Har bir sahifada 5 ta grant
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'city': page_obj,
        'street': street,
        'index': index,
        'language_code': language_code,
    }
    return render(request, 'streets.html', context)


def docs(request):
    index = Index.objects.first()
    language_code = request.LANGUAGE_CODE

    query = request.GET.get('q')
    last_docs = NormativHujjat.objects.all().order_by('id')
    if query:
        docs = NormativHujjat.objects.filter(Q(title__icontains=query) | Q(number__icontains=query)).order_by('-id')
    else:
        docs = NormativHujjat.objects.all().order_by('-id')

    paginator = Paginator(docs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'docs': page_obj,
        'last_docs': last_docs,
        'index': index,
        'language_code': language_code
    }
    return render(request, 'docs.html', context)
