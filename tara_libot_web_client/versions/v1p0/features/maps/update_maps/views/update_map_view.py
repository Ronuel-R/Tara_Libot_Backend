from rest_framework.views import APIView
from .......models.models import Marker
from ..serializers.update_map_serializer import UpdateMarkerSerializer
from rest_framework.response import Response
from constants.http_messages import *
import qrcode
from io import BytesIO

class MarkerListUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        try:
            marker_id = request.query_params.get('id')
            marker = Marker.objects.get(id=marker_id)
        except Marker.DoesNotExist:
            message = 'Marker does not exist'
            status = bad_request
            return Response({"status": status, "message": message, "errors": errors})

        serializer = UpdateMarkerSerializer(instance=marker, data=request.data, partial=True)
        if serializer.is_valid():
            updated_marker = serializer.save()

            if updated_marker.qr_code:
                updated_marker.qr_code.delete(save=False)

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            serialized_marker = UpdateMarkerSerializer(marker).data
            qr.add_data(serialized_marker) 
            qr.make(fit=True)
            qr_image = qr.make_image()

            qr_code_path = f'{updated_marker.id}.png'

            image_bytes = BytesIO()
            qr_image.save(image_bytes, format='PNG')
            image_bytes.seek(0)

            updated_marker.qr_code.save(qr_code_path, image_bytes)

            status = ok
            message = 'Successfully updated Marker'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})