from django.urls import register_converter


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value.__str__()


register_converter(PubDateConverter, 'pubdate')
