from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from rest_framework.authentication import TokenAuthentication
from profiles_api.permissions import UpdateOwnProfile
from profiles_api import permissions, serializers, models
# class helloworld(APIView):
#     """Test API View"""
#     serializer_class = helloSerializers
#     def get(self, request, format=None):
#         """Returns a list of APIView features"""
#         an_apiview = [
#         'Use HTTP methods as function (get, post, patch, put, delete)',
#         'Is similar to a traditional Django View',
#         'Gives you the most contorl over the application logic',
#         'is mapped manually to URLs'
#         ]
#
#         return Response({'message': 'helloworld',
#                         'an_apiview': an_apiview})
#
#     def post(self, request):
#         """Create a hello message with our name"""
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def put(self, request, pk=None):
#         """Handle updating an object"""
#         return Response({'method':'put'})
#
#     def patch(self, request, pk=None):
#         """Handle partial update object"""
#         return Response({'method':'patch'})
#
#     def delete(self, request, pk=None):
#         """Delete an object"""
#         # return Response({'method': 'Delete'})
# class HelloWorldViewSet(viewsets.ViewSet):
#     """Test API ViewSet"""
#     serializer_class = helloSerializers
#
#     def list(self, request):
#         """Return a hello message"""
#         a_viewset = [
#         'user action (list, retrieve, update, partial_update, destroy)',
#         'Automatically maps to URLS using Routers',
#         'Provides more functionlity with less code'
#         ]
#
#         return Response({'message': 'Hello', 'a_viewset': a_viewset})
#
#
#     def create(self, request):
#         """Create a hello message with our name"""
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def update(self, request, pk=None):
#         return Response({'HTTP_method':'put'})
#
#     def partial_update(self, request, pk=None):
#         return Response({'HTTP_method':'patch'})
#
#     def destroy(self, request, pk=None):
#         return Response({'HTTP_method': 'Delete'})
# class UserProfileViewSet(viewsets.ModelViewSet):
#     """Handle creating and updating profile"""
#     serializer_class = serializers.UserProfileSerializer
#     queryset = models.UserProfile.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (UpdateOwnProfile,)
#     filters_backends = (filters.SearchFilter,)
#     search_fields = ('name', 'email',)
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
