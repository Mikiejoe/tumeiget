from rest_framework import serializers
from allauth.account.adapter import get_adapter
from .models import User,FoundId,Searching
from allauth.account.utils import setup_user_email
from django.contrib.auth import authenticate
from dj_rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False,)
    firstname = serializers.CharField(required=False,write_only=True)
    lastname = serializers.CharField(required=False,write_only=True)
    password1 = serializers.CharField(required=False,write_only=True)
    password2 = serializers.CharField(required=False,write_only=True)
    
    def validate_password1(self,password):
        return get_adapter().clean_pasword(password)
    
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError('Passwords dont match')
        return attrs
    
    def custom_signup(self,request,user):
        pass
    
    def get_cleaned_data(self):
        return {
            'fistname':self.validated_data.get('firstname',''),
            'lastname':self.validated_data.get('lastname',''),
            'email':self.validated_data.get('email',''),
            'password1':self.validated_data.get('password1','')   
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.custom_signup = self.get_cleaned_data()
        adapter.save_user(request,user,self)
        self.custom_signup(request,user)
        setup_user_email(request,user,[])
        user.save()
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ('pk','username','email','firstname','lastname','station')
        read_only_fields = ('email',)
        
class FoundIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundId
        fields = '__all__'
        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searching
        fields = '__all__'
