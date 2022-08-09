from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api.serializers import helloSerializers
from rest_framework import status

class helloworld(APIView):
    """Test API View"""
    serializer_class = helloSerializers
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Use HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most contorl over the application logic',
        'is mapped manually to URLs'
        ]

        return Response({'message': 'helloworld',
                        'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Handle partial update object"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'Delete'})
