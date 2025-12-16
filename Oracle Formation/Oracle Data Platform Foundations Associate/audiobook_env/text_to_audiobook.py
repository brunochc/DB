#!/usr/bin/env python3
"""
Script para convertir texto a audiolibro usando Edge TTS (Microsoft Azure Neural Voices)
Alta calidad, rápido y compatible con Python 3.12+
"""

import os
import sys
import re
import asyncio
from pathlib import Path

# Configuración de voz
# Inglés: en-US-AriaNeural, en-US-GuyNeural, en-US-JennyNeural
# Español: es-ES-ElviraNeural, es-ES-AlvaroNeural
VOICE = "en-US-AriaNeural" 

def split_text_by_sections(text_file):
    """Divide el texto en secciones basadas en los capítulos"""
    with open(text_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = []
    current_section = {"title": "Introducción", "content": ""}
    
    lines = content.split('\n')
    for line in lines:
        if re.match(r'^\d+\.\s+[A-Z]', line):
            if current_section["content"].strip():
                sections.append(current_section)
            current_section = {"title": line.strip(), "content": line + "\n"}
        elif re.match(r'^\d+\.\d+\s+', line):
            if current_section["content"].strip():
                sections.append(current_section)
            current_section = {"title": line.strip(), "content": line + "\n"}
        else:
            current_section["content"] += line + "\n"
    
    if current_section["content"].strip():
        sections.append(current_section)
    
    return sections

def clean_text_for_tts(text):
    """Limpia el texto para mejorar la síntesis de voz"""
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

async def generate_audio_edge(text, output_file, voice=VOICE):
    """Genera audio usando Edge TTS"""
    try:
        import edge_tts
        
        print(f"Generando audio: {output_file}")
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        
        print(f"✓ Audio generado: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Error generando audio: {e}")
        return False

async def create_audiobook_async(text_file, output_dir="audiobook_output"):
    """Crea el audiolibro completo (versión asíncrona)"""
    
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Convirtiendo: {text_file}")
    print(f"Usando voz: {VOICE}")
    print(f"Directorio de salida: {output_dir}")
    print(f"{'='*60}\n")
    
    sections = split_text_by_sections(text_file)
    print(f"✓ {len(sections)} secciones encontradas\n")
    
    for i, section in enumerate(sections, 1):
        title = section["title"][:50]
        content = clean_text_for_tts(section["content"])
        
        if len(content) < 50:
            continue
        
        safe_title = re.sub(r'[^\w\s-]', '', title)
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        
        mp3_file = f"{output_dir}/{i:03d}_{safe_title}.mp3"
        
        print(f"\n[{i}/{len(sections)}] {title}")
        print(f"Caracteres: {len(content)}")
        
        await generate_audio_edge(content, mp3_file)
    
    print(f"\n{'='*60}")
    print(f"✓ Audiolibro completado en: {output_dir}")
    print(f"{'='*60}\n")

def main():
    text_file = "OracleDataFoundationsAssociate.txt"
    
    if not os.path.exists(text_file):
        print(f"✗ Error: No se encontró el archivo {text_file}")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("CONVERSOR DE TEXTO A AUDIOLIBRO - Edge TTS")
    print("="*60)
    
    try:
        asyncio.run(create_audiobook_async(text_file))
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
        sys.exit(0)

if __name__ == "__main__":
    main()
