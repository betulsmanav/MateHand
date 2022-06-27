# Generated by Django 4.0.5 on 2022-06-19 10:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='media/image')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtag', to='store.hashtag')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('batch', models.CharField(choices=[('user', None), ('Dr', 'Doctor'), ('Psk', 'psikolog'), ('Dt', 'dentist'), ('Dyt', 'diyetisyen')], default=None, max_length=5)),
                ('profile_avatar', models.ImageField(blank=True, upload_to='media/avatar')),
                ('background_image', models.ImageField(blank=True, upload_to='media/background')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('phone_number', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRoomMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_room_on', models.DateTimeField(auto_now_add=True)),
                ('left_room_on', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_room', to='store.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_room', to='store.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='store.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like_user', to='store.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PostHashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fatma', to='store.hashtag')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='osman', to='store.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='store.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='store.room'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='store.userprofile'),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='store.userprofile')),
                ('follower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='store.userprofile')),
            ],
        ),
    ]