import jwt
from .http_messages import *

class AuthUser():
    def get_token(request):

        token = request.META.get('HTTP_AUTHORIZATION', None)

        if not token:
            return {'errors' : 'Token is not provided','status' : bad_request,'data': {}, 'message' : 'Token error'}

        return token
    
    def get_user(token):

        token = token.split()
        token_bearer = token[0]

        if len(token) == 2:
            access_token = token[1]
        else:
            access_token = None

        if token_bearer == "JWT":
            try:
                payload = jwt.decode(access_token,'secret',algorithms=['HS256'])

            except jwt.ExpiredSignatureError:
                return {'errors': 'Access Token Expired', 'status' : bad_request, 'data': {}, 'message' : 'Token error'}

            except:
                return {'errors': 'Invalid Token', 'status' : bad_request, 'data': {}, 'message' : 'Token error'}

        else:
            return {'errors': 'Invalid Token Bearer', 'status' : bad_request, 'data': {}, 'message' : 'Token error'}

        return payload