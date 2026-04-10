# Tu Periodico IA — Guia Operativa para Agentes

Este documento explica como funciona el sistema completo del periodico. Si eres un agente de Claude Code trabajando en este repo, lee esto primero.

## Que es este proyecto

Un periodico diario de inteligencia artificial escrito por IA, publicado en Telegram (canal principal) y WhatsApp (teaser). El autor es Nerio Gonzalez D', emprendedor latinoamericano. El periodico se publica de lunes a viernes a las 07:00 hora de Ekaterinburg (UTC+5).

**Canal Telegram:** @TUPERIODICOIA (https://t.me/TUPERIODICOIA)
**Bot Telegram:** @TuPeriodicoIA_bot
**Instagram:** @neriogonzalezd
**Web:** neriogonzalezd.com

## Estructura del repositorio

```
ngd-periodico-ia/
├── CLAUDE.md              ← ESTE ARCHIVO. Leelo siempre primero.
├── SKILL.md               ← Especificacion del periodico: formato, plantillas,
│                            reglas de privacidad, calendario. ES LA FUENTE DE
│                            VERDAD del formato y estructura.
├── metodo_isra_bravo.md   ← Metodologia completa de escritura. Como escribir
│                            con el estilo Isra Bravo: formula SLO, tipos de
│                            apertura, tono, anti-patrones, checklist. LEER
│                            SIEMPRE antes de redactar.
├── send_to_telegram.py    ← Script Python para publicar en el canal de Telegram.
│                            Lee periodico_hoy.txt y lo envia. Divide mensajes
│                            largos. Fallback sin Markdown si falla el parseo.
│                            Archiva automaticamente en archivo/.
├── edicion_counter.json   ← Contador de ediciones. Formato: {year, edition,
│                            last_date, format}. Leer antes de generar,
│                            incrementar despues de publicar.
├── periodico_hoy.txt      ← Edicion actual (Telegram). Se sobreescribe cada dia.
├── whatsapp_teaser.txt    ← Teaser actual (WhatsApp). Se sobreescribe cada dia.
└── archivo/               ← Archivo historico de todas las ediciones publicadas.
    ├── periodico_YYYY-MM-DD.txt
    └── whatsapp_YYYY-MM-DD.txt
```

**Todos los archivos se usan activamente.** No hay archivos muertos ni legacy.

## Flujo completo de generacion (paso a paso)

### Paso 1: Preparacion
```
git pull origin main
```
Siempre actualizar el repo antes de generar. El SKILL.md es la fuente de verdad del formato.

### Paso 2: Leer el estado actual
- Leer `edicion_counter.json` para saber el numero de edicion
- Leer `SKILL.md` para tener el formato y reglas actualizadas
- Verificar que dia de la semana es (afecta el enfoque tematico)

### Paso 3: Buscar noticias
- Web search de noticias de IA de las ultimas 24-48 horas
- Seleccionar la noticia mas impactante como PRINCIPAL
- Identificar 5 noticias principales de IA para la seccion "Las 5 de hoy"
- Buscar 3 herramientas de IA nuevas en fuentes confiables (Product Hunt, etc.)
- Preparar un tip practico de Claude/Claude Code para "Tu minuto con Claude"

### Paso 4: Generar el contenido
- Crear historia personal (ver rotacion de tipos en SKILL.md)
- Conectar la historia con la noticia principal
- Aplicar el enfoque tematico del dia (lunes=resumen, martes=herramientas, etc.)
- Si es viernes: formato especial "Top 5 de la semana"
- Escribir con el metodo Isra Bravo (frases cortas, tono directo, opinion fuerte)

### Paso 5: Escribir los archivos
- Guardar version Telegram en `periodico_hoy.txt`
- Guardar teaser WhatsApp en `whatsapp_teaser.txt`
- CRITICO: Ambas versiones deben ser COHERENTES. El teaser es el gancho de la misma historia.

### Paso 6: Publicar
- Ejecutar `send_to_telegram.py` (necesita variables de entorno, ver seccion Credenciales)
- El script archiva automaticamente en `archivo/periodico_YYYY-MM-DD.txt`

### Paso 7: Registrar en Notion
- Crear registro en la base de datos "Tu Periodico IA — Archivo" en Notion
- Campos: Edicion, Fecha, Titular, Historia, Estado, Texto WhatsApp, Texto Telegram, Notas
- El campo "Texto WhatsApp" debe estar listo para que Nerio solo copie y pegue

### Paso 8: Actualizar contador
- Incrementar `edicion_counter.json` (edition + 1, actualizar last_date y format)
- Commit y push al repo

## Credenciales y variables de entorno

El script `send_to_telegram.py` requiere:
- `TELEGRAM_BOT_TOKEN` — Token del bot @TuPeriodicoIA_bot
- `TELEGRAM_CHANNEL_ID` — Chat ID del canal @TUPERIODICOIA

Estas variables deben estar configuradas en el entorno antes de ejecutar el script.

## Reglas criticas (INNEGOCIABLES)

### Privacidad
- NUNCA mencionar ciudades donde vive Nerio (ninguna)
- NUNCA nombres de personas cercanas (pareja, amigos, familiares)
- NUNCA la universidad especifica
- Usar referencias vagas: "mi ciudad", "donde vivo", "mi novia"

### Contenido
- NUNCA inventar noticias — solo informacion real verificada con web search
- NUNCA mencionar "Twitter" — siempre decir "X" o "redes sociales"
- NUNCA emojis dentro del cuerpo de la historia
- Telegram: apuntar a max 5500 caracteres. El script divide automaticamente en partes de max 4000 chars (maximo 2 mensajes). WhatsApp: max 150 palabras.
- NUNCA dar la noticia completa en el teaser de WhatsApp
- NUNCA usar [texto](url) en WhatsApp (no funciona)
- NUNCA abrir con bullets o resumen — siempre abrir con historia personal

### Publicacion
- NUNCA reenviar a Telegram si ya fue publicado. Errores se corrigen en la proxima edicion.
- NUNCA publicar sabados ni domingos
- Siempre hacer git pull antes de generar para tener el SKILL.md actualizado

### Historias personales
- Rotar entre 5 tipos: "Me paso algo", "Vi algo", "Alguien me pregunto", "Cometi un error", "Observacion"
- "Un amigo me dijo/pregunto" maximo 1 vez cada 5-6 ediciones
- Variar con experiencias propias, observaciones, errores, reflexiones
- Nunca repetir la misma estructura de apertura dos dias seguidos

## Formato

El formato detallado (plantillas Telegram y WhatsApp, encabezado obligatorio, reglas de Markdown, enfoque por dia) esta en `SKILL.md`. La metodologia de escritura (estilo Isra Bravo, formula SLO, tipos de apertura, tono, anti-patrones) esta en `metodo_isra_bravo.md`. Leer AMBOS antes de generar una edicion.

### Encabezado (referencia rapida)
```
═══════════════════════════
⚡ *TU PERIODICO IA* ⚡
_La IA que importa. Sin humo._
═══════════════════════════
📅 [Dia] [dia] de [mes], [año]
✍️ Nerio Gonzalez D' — _N° [AÑO].[EDICION]_
```

Este encabezado es IDENTICO en Telegram y WhatsApp. No se modifica nunca.
La historia personal comienza DIRECTAMENTE despues del encabezado (sin separador extra).

### Secciones del periodico (nombres oficiales)
- Historia personal → entrada directa sin separador, metodo Isra Bravo estricto
- "Las 5 de hoy" → 5 noticias mas importantes de IA del dia (NO decir "de la semana")
- "3 herramientas IA nuevas" → herramientas reales buscadas en fuentes confiables
- "Tu minuto con Claude" → mini tip practico con Claude/Claude Code, ejemplo copiable
- "Prompt del dia" → prompt util y nuevo cada dia
- "Palabra" + frase del dia → unificados en un solo bloque
- Footer compacto → links en 1 linea con separador ·

## Notion

El workspace de Notion de Nerio esta conectado a Claude Code. La base de datos "Tu Periodico IA — Archivo" tiene los campos:
- Edicion, Fecha, Titular, Historia, Estado, Texto WhatsApp, Texto Telegram, Notas

El unico paso manual de Nerio es copiar el "Texto WhatsApp" de Notion y pegarlo en sus grupos de WhatsApp. Todo lo demas es automatico.

## Enfoque tematico por dia

| Dia       | Enfoque                                    |
|-----------|--------------------------------------------|
| Lunes     | Resumen del fin de semana + lo que viene    |
| Martes    | Herramientas y productividad con IA         |
| Miercoles | Negocios, startups e inversiones en IA      |
| Jueves    | Investigacion, avances tecnicos y modelos   |
| Viernes   | Top 5 de la semana (formato especial, 500 palabras permitidas) |

El enfoque es una guia, no una regla rigida. Si la noticia mas fuerte del dia no coincide con el enfoque, la noticia manda.

## Troubleshooting

| Problema | Solucion |
|----------|----------|
| Markdown falla en Telegram | El script reintenta sin parse_mode automaticamente |
| Mensaje muy largo | El script divide en partes de max 4000 chars |
| Edicion ya publicada con error | NO reenviar. Corregir para la proxima edicion |
| Formato incorrecto | Hacer git pull y releer SKILL.md |
| Variables de entorno faltantes | Configurar TELEGRAM_BOT_TOKEN y TELEGRAM_CHANNEL_ID |
