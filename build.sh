#!/bin/bash

echo "⚡ Instalando dependencias..."
pip install -r requirements.txt

echo "⚡ Aplicando migraciones de infraestructura primero..."
python manage.py migrate infrastructure --noinput

echo "⚡ Aplicando migraciones del resto de la aplicación..."
python manage.py migrate --noinput

echo "✅ Build completado correctamente."
