# Contexto inicial (conversación del 06/10/2026)

## Estado
**Todavía no hemos empezado a trabajar.** Solo se ha creado la estructura del repo.
Primer paso del próximo chat: comprobar si los plugins están instalados y cargados (lista abajo). El usuario quiere confirmarlo **antes de dar órdenes**: no empezar ninguna tarea hasta entonces.

## El proyecto
- Marca de ropa **de mujer**, venta online directa a la clienta (DTC).
- Tienda en **Shopify** (elegido por rapidez: tallas, stock, pagos, envíos e integración con Meta y TikTok).
- Vende en **Europa**, en varios idiomas.
- El usuario tiene "más o menos lo inicial" de la marca, pero aún no se ha volcado aquí.
- Nombre del repo provisional: `marca-ropa`. Se puede renombrar.

## Decisiones tomadas y por qué
- **Un solo repo, carpetas por área, README corto en cada una**: para no liarse y gastar pocos créditos (solo se abre lo que toca).
- **Publicidad dentro de `campañas/`**: la publicidad de pago casi siempre forma parte de una campaña. Cada campaña tiene `brief.md`, `anuncios.md`, `organico.md` y `resultados.md`; lo aprendido de anuncios va en `campañas/aprendizajes.md`.
- **Sin carpetas por idioma**: un idioma maestro (español, provisional) y traducciones en Shopify (Markets + Translate & Adapt). Lo que cambia por país va en `mercados/`.
- **La web separada de las operaciones**: `web/` es la parte técnica, de la que se hablará mucho, y `operaciones/` lleva el día a día (envíos, devoluciones). Si se modifica el código del tema, vivirá en `web/` y ahí sí podría servir graphify.
- **`produccion/` y `legal-finanzas/` añadidas** tras una investigación corta: son áreas clave de una marca de ropa.
- **Graphify no se usa por ahora**: sirve para código con muchos archivos; aquí hay sobre todo textos y decisiones.

## Lo más importante del sector (investigación corta)
- Tallas y ajuste: primera causa de devoluciones. Guía de tallas con medidas reales desde el principio.
- Producción: empezar subcontratando o con lotes pequeños locales.
- Diseños propios en parte del catálogo: mejor margen y control.
- La recompra da el beneficio: email y comunidad pesan tanto como los anuncios.
- Legal en España (a confirmar con gestor): alta como autónomo o SL, registro de marca en OEPM/EUIPO antes de lanzar, etiqueta textil con composición en castellano, aviso legal, privacidad (RGPD), cookies, desistimiento de 14 días. Para vender en la UE, probablemente IVA por ventanilla única (OSS).

## Plugins
**Fase actual (idea y estructura)**, instalados por el usuario el 06/10, pero el chat que los recomendó no los detectaba (aún no cargados):
- **Product Marketing**: clienta ideal, posicionamiento, competencia, mensajes.
- **strategy-frameworks**: Business Model Canvas, STP, DAFO, Blue Ocean (`/think`).
- **Marketing** (Anthropic): tono de marca, campañas, competencia.

**Más adelante, no instalar aún** (cada plugin añade coste a cada mensaje):
- shopify-ai-toolkit (oficial de Shopify), en la fase web.
- Design (Anthropic): guía de estilo y diseño web.
- Windsor.ai o AdWhispr: análisis de anuncios y anuncios de la competencia.

Ya conectados: Buffer (programar redes), Higgs y ElevenLabs (foto, vídeo, voz).

**Skill propia:** cuando estén definidas la marca y la clienta, crear con skill-creator una skill con la guía de marca, el tono, las tallas y las reglas.

## Pendiente
1. Comprobar los plugins en el chat nuevo.
2. Confirmar el idioma maestro (propuesto: español).
3. Volcar en `marca/` lo que el usuario ya tiene de la marca.
4. Cuando el usuario se ponga manos a la obra: decirle cuántos chats abrir y para qué.
