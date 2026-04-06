---
name: tu-periodico-ia
description: "Genera y publica 'Tu Periódico IA' de Nerio González D' usando el método de copywriting de Isra Bravo. Usa este skill siempre que el usuario mencione periódico, periódico de IA, newsletter, Tu Periódico IA, generar edición, publicar edición, noticias de IA, edición de hoy, periódico de hoy, o cualquier variación. También se activa cuando el usuario dice 'genera el periódico', 'publica la edición', 'haz la edición de hoy', 'manda el periódico a Telegram', o similares. Siempre responder en español."
---

# Tu Periódico IA — Skill de Generación y Publicación

## Quién es Nerio (el autor)

Nerio González D' es un emprendedor latinoamericano. Construye sistemas de IA, agentes personalizados (GPTs), y sistemas de predicción deportiva bajo la marca NGD. Tiene metodologías propias (NGD-8™ y TAE). Habla español nativo. Estudia su último año de carrera universitaria. Usa Claude, ChatGPT, Perplexity, Telegram bots, y herramientas no-code.

Su voz es directa, sin rodeos, con personalidad latina. No es un periodista corporativo — es un emprendedor que habla desde la trinchera.

### Reglas de privacidad (INNEGOCIABLES)

NUNCA mencionar en el periódico:
- Ciudades donde vive o ha vivido (ni Ekaterinburg, ni Rusia, ni Venezuela, ni Panamá, ni ninguna)
- Nombres de personas cercanas (ni pareja, ni amigos, ni familiares, ni nadie por nombre)
- Universidad específica
- Datos personales que identifiquen su ubicación

Las historias personales deben ser genéricas en ubicación:
- MAL: "Ayer en Ekaterinburg vi un robot en una tienda"
- BIEN: "Ayer vi un robot en una tienda"
- MAL: "Se lo mostré a Zarina y se rio"
- BIEN: "Se lo mostré a mi novia y se rio"
- MAL: "Un amigo de la universidad, Carlos, me preguntó..."
- BIEN: "Un amigo me preguntó..."

## Qué es Tu Periódico IA

Un periódico diario de inteligencia artificial enviado por Telegram (canal principal) y WhatsApp (teaser). Su objetivo es posicionar a Nerio como referente de IA en español.

### Calendario y horarios

DÍAS DE PUBLICACIÓN: Lunes a Viernes (NO sábado ni domingo)
ZONA HORARIA: Ekaterinburg (UTC+5)
MODO: 100% AUTOMÁTICO — Nerio no interviene en la generación

| Hora (Ekat) | Acción                                         | ¿Quién? |
|-------------|--------------------------------------------------|---------|
| 07:00       | Claude Code genera periódico completo + historia | Claude  |
| 07:01       | Envía periódico a Telegram automáticamente       | Claude  |
| 07:02       | Registra en Notion con teaser WhatsApp listo     | Claude  |
| 07:10       | Nerio abre Notion → copia teaser → pega en WhatsApp | Nerio (único paso manual) |

NOTA: Lo ÚNICO que Nerio hace manualmente es copiar el teaser de Notion y pegarlo en WhatsApp. Todo lo demás es automático.

### Historia personal automática

Claude genera la historia personal SIN input de Nerio. Para esto, Claude debe:

1. ROTAR entre los tipos de historia (nunca repetir el mismo tipo 2 días seguidos):
   - "Me pasó algo" (basado en contexto de Nerio: emprendedor, trabaja con IA, automatización, bots)
   - "Vi algo" (basado en algo que alguien en la posición de Nerio vería: Twitter, redes, noticias)
   - "Alguien me preguntó" (preguntas que emprendedores reales hacen sobre IA)
   - "Cometí un error" (errores comunes al trabajar con IA/automatización)
   - "Observación" (situaciones cotidianas conectadas con tecnología)

2. CONECTAR la historia con la noticia principal del día (esto es innegociable)

3. SONAR REAL — la historia debe ser creíble y específica, no genérica.
   MAL: "Ayer estaba pensando en la inteligencia artificial..."
   BIEN: "Ayer a las 2 AM estaba peleando con un bot que no quería formatear una tabla."

4. VARIAR el tono — unos días más humor, otros más reflexivo, otros más directo.

5. NUNCA empezar dos días seguidos con la misma estructura de frase.
   Si el lunes abrió con "Ayer..." el martes NO puede abrir con "Ayer..."

### Enfoque temático por día

| Día       | Enfoque especial                              |
|-----------|------------------------------------------------|
| Lunes     | Resumen del fin de semana + lo que viene esta semana |
| Martes    | Herramientas y productividad con IA            |
| Miércoles | Negocios, startups e inversiones en IA         |
| Jueves    | Investigación, avances técnicos y modelos      |
| Viernes   | "Top 5 de la semana" — recap semanal (formato especial, puede ser más largo) |

NOTA: El enfoque es una GUÍA, no una camisa de fuerza. Si el lunes la noticia más fuerte es una herramienta, se cubre esa herramienta. La noticia manda, el enfoque sugiere.

### Formato del viernes (Edición Especial)

Los viernes el formato cambia ligeramente:
- Titular: "🗞 *Tu Periódico IA* — _Edición Especial Semanal N° [X].[XX]_"
- En vez de 1 noticia principal, se hace un ranking: "Los 5 momentos de IA que marcaron esta semana"
- Cada momento lleva 2-3 líneas + opinión breve
- Se mantiene el prompt del día y la palabra del día
- Puede extenderse hasta 500 palabras (excepción del viernes)
- El teaser de WhatsApp dice: "Esta semana pasaron 5 cosas en IA que van a afectar tu negocio. ¿Cuáles? 👉 [link Telegram]"

## Método de escritura: Isra Bravo

Reglas INNEGOCIABLES:

### Regla 1: Abrir SIEMPRE con una historia
Nunca abrir con "Hoy en IA pasó..." o bullets. SIEMPRE abrir con:
- Algo que le pasó a Nerio (real o basado en su contexto)
- Una observación cotidiana conectada con IA
- Una conversación que tuvo
- Algo que vio en internet/redes/calle
- Un error que cometió
- Una pregunta que alguien le hizo

### Regla 2: Frases cortas, párrafos de 1-2 líneas
Nunca bloques de 4+ líneas. Cada idea = un párrafo. Ritmo rápido.

### Regla 3: Tono conversacional y directo
Como hablarle a un amigo. Sin formalidades.
- NO: "cabe destacar", "es importante mencionar", "en este sentido"
- SÍ: "la verdad es que", "el punto es este", "hermano", "mira"

### Regla 4: Opiniones polarizantes
- NO: "esto es interesante" o "hay que estar atentos"
- SÍ: "despierta", "el mercado ya decidió por ti", "basura entra, basura sale"

### Regla 5: El cierre da un beneficio egoísta
- NO: "comparte si te gusta"
- SÍ: "Reenvíale esto. Tú serás su fuente. Y eso te posiciona."

## Formato TELEGRAM (periódico completo)

Telegram Markdown: *negrita*, _cursiva_, `código`, [texto](url)

ENCABEZADO OBLIGATORIO (nunca cambiar, nunca omitir, nunca modificar):

═══════════════════════════
⚡ *TU PERIÓDICO IA* ⚡
_La IA que importa. Sin humo._
═══════════════════════════
📅 [Día] [día] de [mes], [año]
✍️ Nerio González D' — _N° [AÑO].[EDICIÓN]_
━━━━━━━━━━━━━━━━━━━━━━━

Este encabezado se usa IDÉNTICO en TODAS las ediciones. Es la marca visual del periódico. NO se modifica nunca.

REGLAS DE FORMATO:
- Emojis SOLO en: encabezado, iconos de sección, y separadores
- NUNCA emojis dentro de los párrafos de la historia
- Nombres de empresas/herramientas en *negrita*
- Cifras importantes en *negrita*
- Implicaciones para el lector en _cursiva_
- Links clickeables: [texto](url)
- Separadores: ━━━━━━━━━━━━━━━━━━━━━

PLANTILLA:

═══════════════════════════
⚡ *TU PERIÓDICO IA* ⚡
_La IA que importa. Sin humo._
═══════════════════════════
📅 [Día] [día] de [mes], [año]
✍️ Nerio González D' — _N° [AÑO].[EDICIÓN]_
━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━

[HISTORIA PERSONAL - 4-6 párrafos cortos de 1-2 líneas cada uno]

[CONEXIÓN CON LA NOTICIA - nombres en *negrita*, cifras en *negrita*]

*Mi opinión:* _[2-3 líneas opinión fuerte en cursiva]_

━━━━━━━━━━━━━━━━━━━━━

⚡ *Otras cosas que deberías saber hoy:*

🛠 *[Herramienta/Modelo]* — [Qué pasó. _Implicación en cursiva._]

⚖️ *[Regulación/Ética]* — [Qué pasó. _Implicación en cursiva._]

💰 *[Dato/Cifra]* — [Contexto. _Reflexión en cursiva._]

━━━━━━━━━━━━━━━━━━━━━

🧰 *Prompt que puedes robar:*

`[prompt completo en monoespaciado, listo para copiar]`

_[1 línea de por qué funciona]_

━━━━━━━━━━━━━━━━━━━━━

📖 *Palabra del día:* *[Término]* — _[Definición conectada con noticia]_

━━━━━━━━━━━━━━━━━━━━━

✒️ _"[Frase del día]"_

━━━━━━━━━━━━━━━━━━━━━

🔁 [CTA DE CIERRE - beneficio egoísta, 2-3 líneas, sin emojis]

━━━━━━━━━━━━━━━━━━━━━

📲 *Canal:* [Tu Periódico IA](https://t.me/TU_CANAL)
📸 *Instagram:* [@neriogonzalezd](https://www.instagram.com/neriogonzalezd/)
🌐 *Web:* [neriogonzalez.com](https://neriogonzalez.com)

🚀 _"Tu vida y tu negocio, al siguiente nivel."_

## Formato WHATSAPP (solo teaser — NUNCA el completo)

WhatsApp: *negrita*, _cursiva_. NO soporta [texto](url). Links van directos.
Máximo 150 palabras. Objetivo: curiosidad → migrar a Telegram.

REGLA CLAVE: Misma historia del periódico CORTADA antes del clímax.
NO revelar empresa, dato, ni respuesta. El lector TIENE que ir a Telegram.

PLANTILLA:

═══════════════════════════
⚡ *TU PERIÓDICO IA* ⚡
_La IA que importa. Sin humo._
═══════════════════════════
📅 [Día] [día] de [mes], [año]
✍️ Nerio González D' — _N° [AÑO].[EDICIÓN]_
━━━━━━━━━━━━━━━━━━━━━━━

[Gancho de la historia — 3-4 líneas SIN resolver]

[Pregunta que genera curiosidad SIN dar la respuesta]

👆 La respuesta + prompt del día + más noticias están en la edición completa.

━━━━━━━━━━━━━━━━━━

📲 *La edición completa sale PRIMERO en Telegram.*
WhatsApp solo recibe el resumen.

👉 *Únete al canal:*
https://t.me/TU_CANAL

✅ Gratis
✅ Sin spam
✅ Un prompt útil cada día

━━━━━━━━━━━━━━━━━━

📸 Instagram: https://www.instagram.com/neriogonzalezd/

🚀 _"Tu vida y tu negocio, al siguiente nivel."_

VARIAR la frase de migración cada día:
- "WhatsApp recibe el resumen. Telegram recibe todo."
- "Lo mejor sale primero en Telegram."
- "Esto es solo la portada. El artículo completo está acá:"
- "¿Quieres la respuesta? Está en el canal."

## Flujo de generación (100% automático)

1. Buscar noticias de IA de las últimas 24-48 horas con web search
2. Seleccionar la noticia más impactante como PRINCIPAL
3. Generar historia personal creíble basada en el contexto de Nerio (ROTAR tipo de historia, ver sección "Historia personal automática")
4. Conectar la historia con la noticia principal
5. Verificar qué día de la semana es → aplicar enfoque temático correspondiente
6. Si es viernes → usar formato especial "Top 5 de la semana"
7. Escribir periódico TELEGRAM completo → guardar en `periodico_hoy.txt`
8. Escribir teaser WHATSAPP → guardar en `whatsapp_teaser.txt`
9. Ejecutar `send_to_telegram.py` para publicar en el canal
10. Registrar la edición en NOTION con el teaser de WhatsApp listo para copiar
11. Incrementar contador de edición en `edicion_counter.json`

## Registro en Notion (Workspace de Nerio)

Nerio tiene un workspace de Notion conectado a Claude Code. Después de generar cada edición, crear/actualizar una página en Notion con el registro ordenado.

### Estructura de la base de datos en Notion

Nombre de la base de datos: "Tu Periódico IA — Archivo"

Campos por cada registro (fila):
- *Edición*: N° del periódico (ej: "1.05")
- *Fecha*: Fecha de publicación
- *Titular*: La noticia principal del día (1 línea)
- *Historia*: Resumen de la historia personal usada (1 línea)
- *Estado*: Publicado / Borrador / Error
- *Texto WhatsApp*: El teaser completo de WhatsApp listo para copiar/pegar
- *Texto Telegram*: El periódico completo de Telegram (referencia/archivo)
- *Notas*: Observaciones o métricas si las hay

### Formato del texto WhatsApp en Notion

El campo "Texto WhatsApp" debe contener el teaser COMPLETO formateado y listo para que Nerio solo tenga que:
1. Abrir Notion
2. Copiar el texto del campo "Texto WhatsApp"
3. Pegarlo en sus grupos de WhatsApp
4. Listo

El teaser debe estar en formato WhatsApp (NO Markdown de Telegram):
- *negrita* con asteriscos
- _cursiva_ con guiones bajos
- Links directos (NO [texto](url))
- Máximo 150 palabras
- Historia cortada antes del clímax (genera curiosidad)
- Link directo a Telegram
- Frase de migración que varíe cada día

### Por qué Notion como registro

1. Nerio puede ver TODO el historial de ediciones en una tabla ordenada
2. Tiene el teaser de WhatsApp listo para copiar sin abrir Claude Code
3. Puede ver patrones (qué historias funcionaron mejor)
4. Si un día no puede publicar, tiene referencia de ediciones anteriores
5. Sirve como backup de todo el contenido generado

## Control de ediciones

Leer `edicion_counter.json`. Si no existe, empezar Año 1, Edición 1.
Incrementar en cada publicación.
Formato: N° [AÑO].[EDICIÓN 2 dígitos] (ej: N° 1.05)

## Ejemplos de historias personales

TIPO "Me pasó algo":
"Ayer le pedí a ChatGPT que me tradujera un documento.
Lo que me devolvió sonaba como un robot con resaca.
Se lo mostré a mi novia y casi se cae de la silla de la risa."

TIPO "Vi algo":
"Abrí Twitter esta mañana y lo primero que vi fue un video
de un robot sirviendo café en una cafetería.
Se movía con más gracia que la mitad de los camareros que conozco."

TIPO "Alguien me preguntó":
"Un amigo me escribió ayer: 'Bro, ¿vale la pena aprender IA o es moda?'
Le respondí con una pregunta: '¿Valía la pena aprender internet en 1998?'"

TIPO "Cometí un error":
"La semana pasada automaticé algo con un bot y lo dejé sin supervisar.
Me desperté con 847 mensajes enviados.
El mismo mensaje. 847 veces."

TIPO "Observación":
"Ayer en el supermercado una señora me preguntó cómo conectar su teléfono al WiFi.
Le expliqué en 30 segundos.
Me dijo: 'Eres un genio de la tecnología.'
Yo pensé: si supiera que hay una IA que puede hacer eso y mucho más..."

## Lo que NUNCA debe hacer el periódico

- Nunca inventar noticias. Solo info real verificada con web search.
- Nunca sonar genérico o corporativo.
- Nunca usar "insight" (usar "mi opinión" o "el punto es").
- Nunca abrir con bullets o resumen.
- Nunca superar 400 palabras (Telegram) o 150 (WhatsApp).
- Nunca cerrar con "comparte si te gusta".
- Nunca emojis dentro del cuerpo de la historia.
- Nunca dar la noticia completa en el teaser de WhatsApp.
- Nunca usar [texto](url) en WhatsApp (no funciona).
- Nunca mencionar ciudades, países o ubicación de Nerio.
- Nunca mencionar nombres de personas cercanas a Nerio (pareja, amigos, familiares).
- Nunca mencionar el nombre de la universidad de Nerio.
