from django.conf import settings


class db_Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'edxorgs':
            return 'edxappdb'
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'
