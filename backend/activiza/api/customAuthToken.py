from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from activiza.models import Entrenador

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        es_entrenador = False
        
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        
        try:
            Entrenador.objects.get(user = user)
            es_entrenador = True
        except Exception:
            pass
        
        return Response({'token': token.key, 'entrenador': es_entrenador})