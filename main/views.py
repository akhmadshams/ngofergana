from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView

from .models import NTT, NNTName, CityName, Streets, Blog, Grant, NormativHujjat, OAV

def index(request):
    return render(request, 'index.html')


def blog(request):
    blog = Blog.objects.order_by('-id')[1:5]
    last_blog = Blog.objects.latest('id')

    query = request.GET.get('q')

    if query:
        blog = Blog.objects.filter(title__icontains=query).order_by('-id')
    else:
        # Aks holda, barcha Grant obyektlarini olish
        blog = Blog.objects.all().order_by('-id')


    context = {
        'blog': blog,
        'last_blog': last_blog
    }
    return render(request, 'blog.html', context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogChild.html'  # Shablon nomi
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Boshqa modeldan malumotlarni olish
        recent_post = Blog.objects.all()
        context['recent_post'] = recent_post
        return context



def grant(request):
    query = request.GET.get('q')  # Foydalanuvchi tomonidan kiritilgan so'rovi olish
    last_grant = Grant.objects.all().order_by('id')

    # Agar so'rov mavjud bo'lsa, Grant obyektlarini filtratsiya qilish
    if query:
        grant = Grant.objects.filter(title__icontains=query).order_by('-id')
    else:
        # Aks holda, barcha Grant obyektlarini olish
        grant = Grant.objects.all().order_by('-id')

    context = {
        'grant': grant,
        'last_grant':last_grant
    }
    return render(request, 'grant.html', context)


class GrantDetailView(DetailView):
    model = Grant
    template_name = 'grantdetail.html'  # Shablon nomi
    context_object_name = 'grant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Boshqa modeldan malumotlarni olish
        recent_grant = Grant.objects.all()
        context['recent_grant'] = recent_grant
        return context


def oav(request):
    tv = OAV.objects.filter(choice_field='TV')
    gazeta = OAV.objects.filter(choice_field='Gazeta')
    jurnal = OAV.objects.filter(choice_field='Jurnal')
    context = {
        'tv': tv,
        'gazeta': gazeta,
        'jurnal': jurnal,
    }
    return render(request, 'oav.html', context)



class OAVDetailView(DetailView):
    model = OAV
    template_name = 'oavdetail.html'  # Shablon nomi
    context_object_name = 'oav'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Boshqa modeldan malumotlarni olish

        return context




def nnt(request):
    nnt_name = NNTName.objects.all()
    nnt_id = request.GET.get('nnt_name')
    if nnt_id:
        nnt = NTT.objects.filter(nnt=nnt_id)
    else:
        nnt = NTT.objects.filter(name='nom 1')


    context = {
        'nnt_name': nnt_name,
        'nnt': nnt
    }
    return render(request, 'nnt.html', context)



def streets(request):
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

    context = {
        'city': city,
        'street': street,
    }
    return render(request, 'streets.html', context)




def docs(request):
    query = request.GET.get('q')
    last_docs = NormativHujjat.objects.all().order_by('id')
    if query:
        docs = NormativHujjat.objects.filter(Q(title__icontains=query) | Q(number__icontains=query)).order_by('-id')
    else:
        # Aks holda, barcha Grant obyektlarini olish
        docs = NormativHujjat.objects.all().order_by('-id')

    context = {
        'docs': docs,
        'last_docs': last_docs
    }
    return render(request, 'docs.html', context)