from rest_framework import serializers
from ..models import ImagePin
from base.api.serializers import UserPublicSerializer

class ImagePinSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ImagePin
        fields = ('user', 'image', 'description', 'date', 'is_private', 'datetime', 'view_count', 'likes', 'dislikes')

    def get_likes(self, obj):
        return obj.likes.count()
        
    def get_dislikes(self, obj):
        return obj.dislikes.count()