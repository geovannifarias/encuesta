# Generated by Django 4.0.10 on 2023-11-29 07:09

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pregunta', models.SmallIntegerField(choices=[(1, '1'), (2, '2')])),
                ('pregunta_texto', models.TextField()),
                ('id_encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=255)),
                ('numero_telefonico', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='usuario_groups', to='auth.group')),
                ('id_rol', models.ForeignKey(default='COLABORADOR', on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_permissions', to='auth.permission')),
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
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_respuesta', models.CharField(max_length=255)),
                ('respuesta_texto', models.TextField()),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=55)),
                ('texto', models.TextField()),
                ('clasificacion', models.SmallIntegerField(choices=[(1, 'supersatisfecho'), (2, 'satisfecho'), (3, 'insatisfecho')])),
                ('fecha', models.DateField(default=datetime.datetime(2023, 11, 29, 4, 9, 39, 200166))),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='encuesta',
            name='rut_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.usuario'),
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_alternativa', models.CharField(max_length=255)),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEncuesta.pregunta')),
            ],
        ),
    ]
