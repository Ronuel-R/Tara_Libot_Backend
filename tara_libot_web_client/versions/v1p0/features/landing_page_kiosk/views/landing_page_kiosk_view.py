from tara_libot_web_client.models.models import Foods
from tara_libot_web_client.versions.v1p0.features.landing_page_kiosk.serializers.landing_page_kiosk_serializer import LandingPageKioskSerializer
from rest_framework.views import APIView
from constants.http_messages import *
from rest_framework.response import Response
from constants.auth_user import AuthUser
class LandingPageKiosk(APIView):
    def get(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)
        
        try:
            category = request.query_params["category"]
            foods = Foods.objects.filter(category = category).first()

            if foods is None:
                message = 'Dish does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = LandingPageKioskSerializer(foods)
        except:
            foods = Foods.objects.all()
            serializer = LandingPageKioskSerializer(foods,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})