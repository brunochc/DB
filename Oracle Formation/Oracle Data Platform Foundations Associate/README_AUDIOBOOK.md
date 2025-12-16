# Guía para Convertir Texto a Audiolibro (Edge TTS)

Este proyecto convierte el archivo `OracleDataFoundationsAssociate.txt` a un audiolibro en formato MP3 usando **Edge TTS** (voces neuronales de Microsoft Azure).

## 🚀 Inicio Rápido

Simplemente ejecuta el script automático:

```bash
./start_audiobook.sh
```

Este script se encargará de:
1. Crear un entorno virtual aislado (`audiobook_env`)
2. Instalar las dependencias necesarias (`edge-tts`)
3. Generar los archivos de audio en la carpeta `audiobook_output/`

## 📂 Resultados

Los archivos de audio se guardarán en `audiobook_output/` con nombres numerados:

```
audiobook_output/
├── 001_Data_Management_Introduction.mp3
├── 002_Oracle_data_management_strategy.mp3
└── ...
```

## 🗣️ Cambiar la Voz

El script usa por defecto **`en-US-AriaNeural`** (Inglés, voz femenina).

Para cambiarla, edita la línea 15 de `text_to_audiobook.py`:

```python
# Voces en Inglés
VOICE = "en-US-GuyNeural"    # Masculina
VOICE = "en-US-JennyNeural"  # Femenina

# Voces en Español (si el texto estuviera en español)
VOICE = "es-ES-AlvaroNeural" # Masculina
VOICE = "es-ES-ElviraNeural" # Femenina
```

Puedes ver todas las voces disponibles ejecutando:
```bash
./audiobook_env/bin/edge-tts --list-voices
```

## 🛠️ Solución de Problemas

Si el script falla, intenta limpiar el entorno y empezar de cero:

```bash
rm -rf audiobook_env
./start_audiobook.sh
```

## 📋 Requisitos

- Python 3.x
- Conexión a Internet (Edge TTS requiere conexión para generar el audio)
