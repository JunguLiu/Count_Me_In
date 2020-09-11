
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.ImageField(blank=True, upload_to='plan_image', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user', models.CharField(max_length=150)),
                ('from_user', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=150)),
                ('user2', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('calories', models.IntegerField()),
                ('category', models.TextField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('image', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=100)),
                ('workout', models.ManyToManyField(to='main_app.Workouts')),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Comments')),
                ('workouts', models.ManyToManyField(to='main_app.Workouts')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plans')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='wishlists',
            field=models.ManyToManyField(to='main_app.Wishlist'),
        ),
        migrations.AddField(
            model_name='comments',
            name='workout',
            field=models.ManyToManyField(to='main_app.Workouts'),
        ),
    ]
