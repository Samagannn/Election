from rest_framework import serializers
from election_project.models import Candidate, Voter, MyVotes, Appeal, MyAppeal
from account.models import User


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            photo=validated_data['photo'],
            bio=validated_data['bio'],
            address=validated_data['address'],
            committee=validated_data['committee'],
            fractions=validated_data['fractions'],
        )
        return user


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'


class MyVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyVotes
        fields = '__all__'


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'


class MyAppealSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='appeal.subject', read_only=True)
    status = serializers.CharField(source='appeal.status', read_only=True)
    created_at = serializers.DateTimeField(source='appeal.created_at', read_only=True)

    class Meta:
        model = MyAppeal
        fields = ('subject', 'created_at', 'status', 'appeal')

    def create(self, validated_data):
        user = self.context['request'].user
        appeal = validated_data.get('appeal')

        my_appeal = MyAppeal.objects.create(user=user, appeal=appeal)
        return my_appeal
