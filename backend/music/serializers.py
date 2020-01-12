from rest_framework import serializers

from music.models import Song, Musician, Label


class MusicianAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('alias', 'year_of_birth')


class SongListSerializer(serializers.ModelSerializer):
    producer = MusicianAliasSerializer(read_only=True, many=True)
    label = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'producer', 'features', 'label', 'genre']
        ## keinen producer_alias erzeugen NUR producer !!!

    def get_label(self, obj):
        return obj.label.name if obj.label else ''

class SongFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class LabelListSerializer(serializers.ModelSerializer):
    producer = serializers.SerializerMethodField()

    class Meta:
        model = Label
        fields = '__all__'

    def get_producer(self, obj):
        if obj:
            return {x.alias for x in obj.producer.all()}

class LabelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']

class MusicianListSerializer(serializers.ModelSerializer):
    label = LabelNameSerializer(read_only=True, many=True)

    class Meta:
        model = Musician
        fields = '__all__'

class MusicianFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class MusicianIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id']

class LabelFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = [field.name for field in model._meta.fields]
        fields.append('producer')

class LabelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']
