from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    email = serializers.EmailField(required=True)


    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password":  {"write_only": True}
        }


    def save(self):
        user = CustomUser(
            email = self.validated_data["email"],
            username = self.validated_data["username"]
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"Error": "Both passwords  must match."})
        
        user.set_password(password)
        user.save()
        return user