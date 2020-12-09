# Generated by Django 3.1.2 on 2020-12-08 00:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0016_auto_20201208_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_parent', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_subscribed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='editari.user')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editari.school')),
                ('student_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editari.schoolclasse')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('to_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.schoolclasse')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAndSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_grade', models.CharField(max_length=4)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.subject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.student')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(max_length=10)),
                ('is_online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teacher', serialize=False, to='editari.user')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('s_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editari.schoolclasse')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editari.school')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.teacher'),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='parent', serialize=False, to='editari.user')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='editari.student')),
            ],
        ),
        migrations.CreateModel(
            name='CTSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=4)),
                ('student_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.studentandsubject')),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.schoolclasse')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editari.teacher')),
            ],
        ),
    ]
