from modeltranslation.translator import register, TranslationOptions
from .models import NTT, NNTName, CityName, Blog, Grant, NormativHujjat, OAV, Index


@register(NNTName)
class NNTNameModelTranslation(TranslationOptions):
    fields = ('name',)

@register(NTT)
class NNTModelTranslation(TranslationOptions):
    fields = ('name', 'director', 'purpose', 'direction', 'projects', 'address')

@register(CityName)
class CityNameModelTranslation(TranslationOptions):
    fields = ('name',)


@register(Blog)
class BlogModelTranslation(TranslationOptions):
    fields = ('title', 'body')


@register(Grant)
class GrantModelTranslation(TranslationOptions):
    fields = ('title', 'body')


@register(NormativHujjat)
class NormativHujjatModelTranslation(TranslationOptions):
    fields = ('title', 'number')


@register(OAV)
class OAVModelTranslation(TranslationOptions):
    fields = ('name', 'body')


@register(Index)
class IndexTranslation(TranslationOptions):
    fields = ('title', )
