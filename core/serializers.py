from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Perfil

class CadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    tipo = serializers.CharField(write_only=True)
    razao_social = serializers.CharField(required=False, allow_blank=True)
    cnpj = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tipo', 'razao_social', 'cnpj']

    def create(self, validated_data):
        tipo = validated_data.pop('tipo', 'usuario')
        razao_social = validated_data.pop('razao_social', '')
        cnpj = validated_data.pop('cnpj', '')

        # Cria o usuário padrão do Django (salva na tabela auth_user do Supabase)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Cria o perfil vinculado com os dados adicionais
        Perfil.objects.create(
            user=user,
            tipo=tipo,
            razao_social=razao_social if tipo == 'empresa' else '',
            cnpj=cnpj if tipo == 'empresa' else ''
        )

        return user