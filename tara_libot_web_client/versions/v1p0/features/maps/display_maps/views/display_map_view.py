from rest_framework.views import APIView
from .......models.models import Marker
from ..serializers.display_map_serializer import DisplayMarkerSerializer
from rest_framework.response import Response
from constants.http_messages import *


class MarkerListDisplayView(APIView):
    def get(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None
        
        try:
            id = request.query_params["id"]
            markers = Marker.objects.filter(id = id).first()

            if markers is None:
                message = 'Marker  does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})
            serializer = DisplayMarkerSerializer(markers)
        except:
            markers = Marker.objects.all()
            serializer = DisplayMarkerSerializer(markers, many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})