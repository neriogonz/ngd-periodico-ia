#!/usr/bin/env python3
"""
Tu Periódico IA — Envío a Telegram
Uso: python send_to_telegram.py
Lee el archivo periodico_hoy.txt y lo envía al canal.
"""

import os
import sys
import requests
from datetime import datetime


def send_to_telegram(text, token, chat_id):
    """Envía mensaje a Telegram. Divide si es muy largo."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    max_len = 4000

    if len(text) <= max_len:
        messages = [text]
    else:
        sections = text.split("\n\n")
        messages = []
        current = ""
        for section in sections:
            if len(current) + len(section) + 2 > max_len:
                if current:
                    messages.append(current.strip())
                current = section
            else:
                current += "\n\n" + section if current else section
        if current:
            messages.append(current.strip())

    success = True
    for i, msg in enumerate(messages):
        payload = {
            "chat_id": chat_id,
            "text": msg,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }

        response = requests.post(url, json=payload, timeout=30)

        if response.status_code == 200:
            print(f"✅ Parte {i+1}/{len(messages)} enviada")
        else:
            print(f"❌ Error parte {i+1}: {response.text}")
            # Reintentar sin Markdown si falla el parseo
            if "can't parse" in response.text.lower():
                payload.pop("parse_mode")
                retry = requests.post(url, json=payload, timeout=30)
                if retry.status_code == 200:
                    print(f"✅ Parte {i+1} enviada (sin formato)")
                else:
                    success = False
            else:
                success = False

    return success


def main():
    # Obtener credenciales
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHANNEL_ID", "")

    if not token or not chat_id:
        print("❌ Faltan variables de entorno:")
        if not token:
            print("   - TELEGRAM_BOT_TOKEN")
        if not chat_id:
            print("   - TELEGRAM_CHANNEL_ID")
        sys.exit(1)

    # Leer el periódico
    filename = "periodico_hoy.txt"
    if not os.path.exists(filename):
        print(f"❌ No encontré {filename}")
        print("   Crea el archivo con el contenido del periódico primero.")
        sys.exit(1)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        print("❌ El archivo está vacío")
        sys.exit(1)

    print(f"📰 Enviando periódico ({len(content)} caracteres)...")
    
    if send_to_telegram(content, token, chat_id):
        print("🎉 ¡Periódico publicado en Telegram!")
        
        # Archivar
        today = datetime.now().strftime("%Y-%m-%d")
        os.makedirs("archivo", exist_ok=True)
        archive = f"archivo/periodico_{today}.txt"
        with open(archive, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"💾 Archivado en: {archive}")
    else:
        print("❌ Hubo errores al enviar. Revisa los mensajes arriba.")
        sys.exit(1)


if __name__ == "__main__":
    main()
