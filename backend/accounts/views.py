from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
import uuid


class CreateListRoles(APIView):
    """
    CreateListRoles class handles the creation and listing of roles.

    POST: Create a new role.
    GET: List all roles.
    """
    permission_classes = [IsAdminUser]
    
    def post(self, request: Request):
        """
        POST method to create a new role.
        """
        data = request.data
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        """
        GET method to list all roles.
        """
        queryset = Role.objects.all()
        serializer = RoleSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateRole(APIView):
    """
    RetrieveUpdateRole class handles the retrieval and update of a role.

    GET: Retrieve detailed information about a specific role.
    PUT: Update role information (allows partial updates).
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request: Request, pk):
        """
        GET method to retrieve detailed information about a specific role by using its id.
        """
        try:
            queryset = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RoleSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        """
        PUT method to update role information (allows partial updates).
        """
        try:
            queryset = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response({"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = RoleSerializer(queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CreateUsers(APIView):
    """
    CreateUsers class handles the creation of user accounts.

    POST: Create a new user account and send a confirmation email.
    """
    permission_classes = [AllowAny]

    def post(self, request: Request):
        """
        POST method to create a new user account and send a confirmation email.
        """
        data = request.data
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            # Send a confirmation email with a confirmation link
            subject = 'Confirm your email address'
            message = 'Click the link to confirm your email address'
            from_email = 'abiolaadedayo1993@gmail.com'
            recipient_list = [user.email]

            # Generate a confirmation URL
            
            confirmation_url = f"http://127.0.0.1:8000/api/v1/confirm_email?user_id={user.id}&token={user.confirm_email_token}/"

            message += f'\n\n{confirmation_url}'

            send_mail(subject, message, from_email, recipient_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsers(APIView):
    """
    ListUsers class handles the listing of user accounts.

    GET: List all user accounts (requires admin authentication).
    """
    permission_classes = [IsAdminUser]
    
    def get(self, request: Request):
        """
        GET method to list all user accounts (requires admin authentication).
        """
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDeleteUser(APIView):
    """
    RetrieveUpdateDeleteUser class handles the retrieval, update, and deletion of user accounts.

    GET: Retrieve detailed information about a specific user account.
    PUT: Update user account information (allows partial updates).
    DELETE: Delete a specific user account.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request, pk):
        """
        GET method to retrieve detailed information about a specific user account by using its id.
        """
        try:
            
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(instance=queryset)
        user = request.user
        if (user.email != queryset.email):
            return Response({"error": "User Not Authorized"}, status=status.HTTP_403_FORBIDDEN)
    
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        """
        PUT method to update user account information (allows partial updates).
        """
        try:
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        if (user.email != queryset.email):
            return Response({"error": "User Not Authorized"}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        serializer = CustomUserSerializer(queryset, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            queryset = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if (user.email != queryset.email):
            return Response({"error": "User Not Authorized"}, status=status.HTTP_403_FORBIDDEN)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserConfirmEmailAddress(APIView):
    """
    UserConfirmEmailAddress class handles the confirmation of a user's email address.

    GET: Confirm a user's email address with a valid token.
    """
    permission_classes = [AllowAny]

    def get(self, request: Request):
        """
        GET method to confirm a user's email address with a valid token.
        """
        user_id= request.query_params.get("user_id")
        confirm_email_token = request.query_params.get("token")
        
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if (user_id != str(user.pk) or confirm_email_token != str(user.confirm_email_token)):
            return Response({"error": "User Not Authorized"}, status=status.HTTP_403_FORBIDDEN)
        
        if (confirm_email_token == str(user.confirm_email_token)):
            user.confirm_email_token = None
            user.save()
            return Response({"Message": "User email confirmed"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    

class UserForgetPassword(APIView):
    """
    UserForgetPassword class handles the initiation of the forget password process.

    GET: Initiate the forget password process by sending an email with a reset password link.
    """
    permission_classes = [AllowAny]

    def get(self, request: Request):
        """
        GET method to initiate the forget password process by sending an email with a reset password link.
        """
        email = request.query_params.get("email")
        try:
            user = CustomUser.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        
        # Send a confirmation email with a forget password link
        subject = 'Reset your password'
        message = 'Click the link to reset your password'
        from_email = 'abiolaadedayo1993@gmail.com'
        recipient_list = [email]

        # Generate a forget password URL
            
        forget_password_url = f"http://127.0.0.1:8000/api/v1/reset_password?user_id={user.id}&token={user.reset_password_token}/"

        message += f'\n\n{forget_password_url}'

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Email not sent: {str(e)}", status=status.HTTP_400_BAD_REQUEST)


class UserResetPassword(APIView):
    """
    UserResetPassword class handles the reset of a user's password.

    PUT: Reset a user's password with a valid token.
    """
    permission_classes = [AllowAny]

    def put(self, request: Request):
        """
        PUT method to reset a user's password with a valid token.
        """
        user_id = request.query_params.get("user_id")
        reset_password_token = request.query_params.get("token")

        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        
        if (user_id != str(user.id) or reset_password_token != str(user.reset_password_token)):
            return Response({"error": "User Not Authorized"}, status=status.HTTP_403_FORBIDDEN)
        
        if (reset_password_token == str(user.reset_password_token)):
            user.reset_password_token = uuid.uuid4()
            data = request.data
            serializer = CustomUserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
