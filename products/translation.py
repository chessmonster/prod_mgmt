from modeltranslation.translator import translator, TranslationOptions
from products.models import Product

class ProductsTranslationOptions(TranslationOptions):
    fields = ('display_name', )
    required_languages = ('en', 'fi',)
    fallback_values = ('translation unavailable')

translator.register(Product, ProductsTranslationOptions)
