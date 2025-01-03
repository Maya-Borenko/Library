from rest_framework import serializers
from library.library_models.models import Book, Like, SavedBook, Recommendation, User
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SavedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedBook
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'write_only_fields': True}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
