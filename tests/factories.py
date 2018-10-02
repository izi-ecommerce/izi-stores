import factory
from izi.core.loading import get_model
from izi.test.factories import CountryFactory


class StoreFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('stores', 'Store')


class StoreAddressFactory(factory.DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = get_model('stores', 'StoreAddress')


class StoreGroupFactory(factory.DjangoModelFactory):

    class Meta:
        model = get_model('stores', 'StoreGroup')


class StoreStockFactory(factory.DjangoModelFactory):

    class Meta:
        model = get_model('stores', 'StoreStock')
