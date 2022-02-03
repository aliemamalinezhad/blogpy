from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=128)
    cover = serializers.CharField(required=True, max_length=256)
    content = serializers.CharField(required=True, max_length=2048)
    created_at = serializers.DateTimeField(required=True)


class SubmitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128, required=True)
    cover = serializers.FileField(required=True)
    content = serializers.CharField(max_length=2048, required=True)
    category_id = serializers.IntegerField(required=True)
    author_id = serializers.IntegerField(required=True)
    promote = serializers.BooleanField(required=True)


class UpdateArticleCoverSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True)
    cover = serializers.FileField(required=True)


class DeleteArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True)
