# Nesma (repo marca-ropa)

Marca de ropa de mujer con tienda online (Shopify) que vende en Europa.

**ESTADO:** empezado (07/10/2026).

## Decisiones globales (afectan a todos los sectores)
- Nombre de marca: **Nesma** (07/10/2026). Dominio pendiente.
- Nicho: moda musulmana/modesta de mujer, Europa + UK.
- Idioma maestro: español.
- Identidad de marca aprobada: `marca/identidad.md` (clienta, tono, paleta, glosario). Todos los textos e imágenes la siguen.
- Diferencia principal: **largos por altura (petite/regular/tall) + tejidos que no transparentan** → afecta a Producto y Producción.
- Precio: premium accesible (cifras en `producto/`).
- Logo (boceto): "nesma" con la "s" como pliegue terracota; icono = la "s" sola. Archivos en `marca/logo/` → para web, redes y etiquetas.
- Pendiente para Mercados: *tu* o *vous* en francés.

**Lee primero `docs/contexto_inicial.md`**: resume la conversación que creó este repo.

## Reglas
- Respuestas breves, en español.
- **Regla muy importante — un chat por carpeta:** al empezar, el usuario dice en qué carpeta trabaja el chat (si no lo dice, preguntarlo). El chat solo escribe en su carpeta y puede leer las demás. Si el usuario pide o habla de algo de otra carpeta, avisarle siempre y decirle qué chat usar. El chat **General** coordina: `docs/`, `CLAUDE.md`, `BITACORA.md` y temas que tocan varias carpetas.
- Las traducciones se hacen en Shopify, no en carpetas por idioma.
- Toda decisión o cambio va en una línea en `BITACORA.md`, en el mismo commit.
- **Excepción a la regla de carpeta:** si una decisión afecta a otros sectores, cualquier chat añade una línea en "Decisiones globales" (arriba) y en `BITACORA.md`. Este archivo se carga en todos los chats, así que todos se enteran.
- Ahorrar créditos: abrir solo la carpeta de la tarea; cada carpeta tiene un `README.md` corto con propósito y estado.
- Este archivo se carga en cada chat: mantenerlo corto. Lo largo va en `docs/`.

## Mapa
| carpeta | qué va |
|---|---|
| `marca/` | nombre, logo, paleta, tono, clienta ideal, posicionamiento |
| `producto/` | colecciones, drops, tallas, tejidos, fichas, precios y márgenes |
| `produccion/` | proveedores, fabricación, mínimos, plazos, calidad |
| `web/` | Shopify: tema, apps, páginas, SEO técnico, integraciones |
| `operaciones/` | stock, envíos, devoluciones, atención al cliente |
| `mercados/` | países, idiomas, glosario de traducción, tallas EU, monedas, IVA (OSS) |
| `campañas/` | una subcarpeta por campaña (incluye la publicidad de pago) |
| `social/` | calendario y posts orgánicos fuera de campañas |
| `contenido/` | briefs y prompts de foto, vídeo y voz |
| `legal-finanzas/` | forma jurídica, registro de marca, etiquetado, políticas, costes |
| `docs/` | notas largas y contexto |
