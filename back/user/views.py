from rest_framework import generics
from .models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from firebase_admin import auth
from django.utils.text import slugify
from django.core.files.storage import default_storage
from firebase_admin import db
from rest_framework.response import Response
from rest_framework import status

class CreateListUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        user_fields = ["name", "username", "email", "password", "url_photo", "bio"]

        for field in user_fields:
            if field not in data:
                return JsonResponse({"error": f"{field} field is required"}, status=400)

        try:
            user =  auth.create_user(
                email=data["email"],
                password=data["password"],
            )

            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                photo_name = slugify(photo.name)
                file_path = f'profile_photos/{photo_name}'
                default_storage.save(file_path, photo)

                url_photo= default_storage.url(file_path)

            else:
                url_photo = None

            # Salvar os dados do usuário no Firebase Realtime Database
            ref = db.reference('/users')  # Define a referência ao nó 'users' no Firebase
            ref.child(user.uid).set({
                'name': data["name"],
                'username': data["username"],
                'email': data["email"],
                'url_photo': url_photo,
                'bio': data["bio"],
            })
            return JsonResponse({
                'uid': user.uid,
                'email': data['email'],
                'name': data['name'],
                'url_photo': data['url_photo']
            }, status=201)

        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    def list(self, request, *args, **kwargs):
        try:
            ref = db.reference('/users')
            users = ref.get()


            if users is None:
                return JsonResponse({'users': []}, status=200)
            
            users_list = []

            for uid, user_data in users.items():
                user_data['uid'] = uid
                users_list.append(user_data)

            return JsonResponse({'users': users_list}, status=200)
    
        except Exception as e:
           return JsonResponse({"error": str(e)}, status=500)

class RetriveUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs['uid']

        try:
            ref = db.reference(f'/users/{user_id}')
            user_data = ref.get()

            if not user_data:
                return JsonResponse({'error': 'User not found'}, status=404)

            return JsonResponse({'user': user_data, 'uid': user_id}, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    def update(self, request, *args, **kwargs):
        user_id = kwargs['uid']
        data = request.data

        try:
            user = auth.get_user(user_id)

            auth.update_user(user_id, email=data.get('email'))

            ref = db.reference(f'/users/{user_id}')
            ref.update(data)

            return JsonResponse({'user': data, 'uid': user_id}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_id = kwargs['uid']

        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            auth.delete_user(user_id)

            ref = db.reference(f'/users/{user_id}')
            ref.delete()

            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
