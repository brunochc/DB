#!/bin/bash
# Script de instalación rápida para Coqui TTS

echo "=========================================="
echo "INSTALACIÓN DE COQUI TTS - AUDIOBOOK"
echo "=========================================="
echo ""

# Instalar ffmpeg
echo "📦 Instalando ffmpeg..."
sudo apt-get update
sudo apt-get install -y ffmpeg

# Instalar dependencias de Python
echo ""
echo "🐍 Instalando dependencias de Python..."
pip3 install --user TTS pydub

echo ""
echo "✅ Instalación completada"
echo ""
echo "Para ejecutar el script:"
echo "  python3 text_to_audiobook.py"
echo ""
