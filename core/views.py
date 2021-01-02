from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from .serializers import PlantSerializer, Plant, UserSerializer, User, RegisterSerializer


class PlantListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class PlantListView(generics.ListAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# def user_login(request, *args, **kwargs):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         print("Successfully logged in!")
#     else:
#         redirect("/")


# class PlantView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PlantSerializer
#     queryset = Plant.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class PlantView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         plants = Plant.objects.all()
#         serializer = PlantSerializer(plants, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         plant_data = request.data
#         serializer = PlantSerializer(data=plant_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
