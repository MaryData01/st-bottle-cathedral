from rest_framework import serializers
from campuses.models import Campus
from groups.models import MinistryGroup, GroupCategory
from events.models import Event
from sermons.models import Sermon

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class GroupCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCategory
        fields = '__all__'

class MinistryGroupSerializer(serializers.ModelSerializer):
    category = GroupCategorySerializer(read_only=True)
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = MinistryGroup
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

class SermonSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)

    class Meta:
        model = Sermon
        fields = '__all__'
