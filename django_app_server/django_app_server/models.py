from rest_framework import serializers


class Task(object):
    def __init__(self, id, title, owner, status):
        self.id = id
        self.title = title
        self.owner = owner
        self.status = status


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'owner', 'status')
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    owner = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=('New', 'InProgress', 'Done'), default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance