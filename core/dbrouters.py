from django.contrib.auth.models import User
...
class MyDBRouter(object):

    def db_for_read(self, user, **hints):
        """ reading SomeModel from otherdb """
        if user == User.objects.filter(username='demo'):
            return 'otherdb'
        return None

    def db_for_write(self, user, **hints):
        """ writing SomeModel to otherdb """
        if user == User.objects.filter(username='demo'):
            return 'otherdb'
        return None
