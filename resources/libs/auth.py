from rest_framework_jwt import views as jwt_views
from django.forms.models import model_to_dict
from rest_framework import status
from django.contrib.auth.models import User

class UserLoginViewJWT(jwt_views.ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        response =  super().post(request, *args, **kwargs)
        username = request.data.get("username")
        allowed_fields = ("first_name","last_name","last_login","is_active","username")
        if response.status_code == status.HTTP_200_OK:            
            user = User.objects.filter(username=username).only(*allowed_fields).first()
            user_dict = { k:v  for k,v in model_to_dict(user).items() if k in allowed_fields }
            response.data.update( {"user":user_dict} )
            print(response.data)

        return response
