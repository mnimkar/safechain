from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(ModelSerializer):

    password = CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )