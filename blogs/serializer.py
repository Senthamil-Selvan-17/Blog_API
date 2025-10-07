from rest_framework import serializers
from .models import Blog
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content','created_date','comments']
    comments = CommentSerializer(many = True, read_only = True)