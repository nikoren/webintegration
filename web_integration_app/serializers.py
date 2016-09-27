# from web_integration_app.models import SkuToUpcToProductMap, Chain, chain_to_steps, step_to_schema
from rest_framework import serializers
from web_integration_app.models import Chain,Step
from django.contrib.auth.models import User
import json




class ChainSerialiazer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    steps = serializers.HyperlinkedIdentityField(many=True,  view_name='step-detail')

    class Meta:
        fields = ('url','name', 'created', 'type', 'steps', 'owner')
        model = Chain


class StepSerializer(serializers.HyperlinkedModelSerializer):

    # def validate_integration_data(self, input_data):
    #     try:
    #         parsed_sku_to_upc = json.loads(input_data, encoding='utf-8')
    #     except Exception as e:
    #         raise serializers.ValidationError("Integration data is not valid json, {}".format(e.args[0]))
    #
    #     return input_data

    # def validate_integration_data(self, data):
    #     print(data, type(data))
    #     return data

    extra_kwargs = {'integration_data': {'write_only': True}}

    integration_data = serializers.JSONField(binary=True)
    chain = serializers.HyperlinkedRelatedField(queryset=Chain.objects.all(), view_name='chain-detail')

    class Meta:
        model = Step
        fields = ('url', 'name', 'created', 'chain', 'step_type', 'integration_data')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # chain is reverse relation on User model , so it won't be included automatically when using ModelSerializer
    chains = serializers.HyperlinkedIdentityField(many=True,view_name='chain-detail')

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'chains')