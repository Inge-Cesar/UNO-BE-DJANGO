

echo "⚡ Instalando dependencias..."
pip install -r requirements.txt

echo "⚡ Aplicando migraciones de infraestructura primero..."
python manage.py migrate infrastructure --noinput

echo "⚡ Aplicando migraciones del resto de la aplicación..."
python manage.py migrate --noinput

# Crear superusuario solo si no existe
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-admin}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-admin@example.com}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-admin123}

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists(): \
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell

echo "✅ Build completado correctamente."
