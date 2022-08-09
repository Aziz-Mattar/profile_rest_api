from rest_framework.views import APIView
from rest_framework.response import Response


class helloworld(APIView):
    """Test API View"""

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
