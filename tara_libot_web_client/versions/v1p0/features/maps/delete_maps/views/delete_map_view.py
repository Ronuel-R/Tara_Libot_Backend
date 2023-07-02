from rest_framework.views import APIView
from .......models.models import Marker
from rest_framework.response import Response
from constants.http_messages import * 
from django.core.exceptions import ObjectDoesNotExist

class MarkerListDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None


        if "id" in request.query_params:
            id = request.query_params["id"]

            try:
                markers = Marker.objects.get(id = id)
            except ObjectDoesNotExist:
                message = 'Marker with id {} does not exist'.format(id)
                status = bad_request
                return Response({"status": status, "message": message, "data": data, "errors": errors})

            if markers.qr_code:
               markers.qr_code.delete(save=False)
        
            markers.qr_code = None
            markers.save()
            markers.delete()

            message = 'Successfully Deleted Marker'
            status = ok
        else:
            message = 'Invalid Format'
            status = bad_request
        return Response({"status": status , "message": message , "data": data, "errors":errors})