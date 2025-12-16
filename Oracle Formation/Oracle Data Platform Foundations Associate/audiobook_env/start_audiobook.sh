#!/bin/bash

# Definir directorio del entorno virtual
VENV_DIR="audiobook_env"

echo "============================================================"
echo "   CONFIGURACIÓN AUTOMÁTICA DE ENTORNO VIRTUAL"
echo "============================================================"

# 1. Crear entorno virtual
if [ -d "$VENV_DIR" ] && [ ! -f "$VENV_DIR/bin/pip" ]; then
    echo "⚠️  Entorno virtual corrupto detectado. Recreando..."
    rm -rf "$VENV_DIR"
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creando entorno virtual en $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "❌ Error creando entorno virtual. Asegúrate de tener python3.12-venv instalado:"
        echo "   sudo apt install python3.12-venv"
        exit 1
    fi
    echo "✅ Entorno creado."
else
    echo "✅ El entorno virtual ya existe."
fi

# 2. Instalar dependencias usando el pip del entorno explícitamente
echo "⬇️  Verificando dependencias..."
VENV_PYTHON="$VENV_DIR/bin/python3"
VENV_PIP="$VENV_DIR/bin/pip"

# Actualizar pip
"$VENV_PIP" install --upgrade pip > /dev/null 2>&1

# Instalar edge-tts
if ! "$VENV_PYTHON" -c "import edge_tts" &> /dev/null; then
    echo "📦 Instalando Edge TTS..."
    "$VENV_PIP" install edge-tts
    echo "✅ Dependencias instaladas."
else
    echo "✅ Dependencias ya instaladas."
fi

# 3. Ejecutar el script principal con el python del entorno
echo ""
echo "🚀 Iniciando conversor..."
echo "============================================================"
"$VENV_PYTHON" text_to_audiobook.py
