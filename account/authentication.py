
from django.contrib.auth.models import User

# AUTHENTICATION_BACKENDS- its a class provide two method 1.authenticate(request, user) and 2.get_user(user-id)
class EmailAuthBackend(object):
    # 1.authenticate(request, user)
    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    # 2.get_user(user-id)
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None