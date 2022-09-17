from rest_framework import serializers
from ..models import User


class RegistrationSerializer(serializers.ModelSerializer):
    # adding password field here
    # because this field is not present in the user model
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password']
    
    def validate(self, attrs):
        print("\nNOW PRINTING THE attrs:")
        print(attrs)
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        # validate username
        if not username.isalnum():
            raise serializers.ValidationError('Username Error')
        return attrs 
    
    # called when serializer.save() is called
    def create(self, validated_data):
        print("\nPRINTING VALIDATED DATA")
        return User.objects.create_user(**validated_data)
