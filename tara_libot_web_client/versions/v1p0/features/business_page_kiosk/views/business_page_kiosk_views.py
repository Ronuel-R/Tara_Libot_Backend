from tara_libot_web_client.models.models import Business
from tara_libot_web_client.versions.v1p0.features.business_page_kiosk.serializers.business_page_kiosk_serializers import BusinessKioskSerializer
from rest_framework.views import APIView
from constants.http_messages import *
from rest_framework.response import Response
from constants.auth_user import AuthUser

class BusinessKioskViews(APIView):
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
            id = request.query_params["id"]
            foods = Business.objects.filter(id = id).first()

            if foods is None:
                message = 'Business does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = BusinessKioskSerializer(foods)
        except:
            foods = Business.objects.all()
            serializer = BusinessKioskSerializer(foods,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})