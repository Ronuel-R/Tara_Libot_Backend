from tara_libot_web_client.models.models import Foods
from tara_libot_web_client.versions.v1p0.features.landing_page_kiosk.serializers.landing_page_kiosk_serializer import LandingPageKioskSerializer
from rest_framework.views import APIView
from constants.http_messages import *
from rest_framework.response import Response

class LandingPageKiosk(APIView):
    def get(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        try:
            id = request.query_params["id"]
            foods = Foods.objects.filter(id = id).first()

            if foods is None:
                message = 'Ownership Record Card does not exist'
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