from rest_framework.views import APIView
from .......models.models import Marker
from ..serializers.create_map_serializer import CreateMarkerSerializer
from rest_framework.response import Response
from constants.http_messages import *
import qrcode
from io import BytesIO

class MarkerListCreateView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        serializer = CreateMarkerSerializer(data=request.data)
        if serializer.is_valid():
            marker = serializer.save()

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            serialized_marker = CreateMarkerSerializer(marker).data
            qr.add_data(serialized_marker)  
            qr.make(fit=True)
            qr_image = qr.make_image()

            qr_code_path = f'{marker.id}.png'

            image_bytes = BytesIO()
            qr_image.save(image_bytes, format='PNG')
            image_bytes.seek(0)

            marker.qr_code.save(qr_code_path, image_bytes)

            status = created
            message = 'Successfully Created Marker'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
