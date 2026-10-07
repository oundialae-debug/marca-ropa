# Plan de la tienda Shopify de Nesma (v1, 07/10/2026)

Objetivo: tienda montada y diseñada en **modo privado** (con contraseña) hasta que llegue la primera colección. Tema gratuito **Horizon**.

## Fase 1 — Alta de la cuenta (la hace la usuaria)
1. Crear cuenta en shopify.com con el email de la marca. Nombre de tienda: **Nesma**. País: España. Moneda base: EUR.
2. Elegir el plan **Basic** al acabar la prueba (oferta actual: 3 días gratis y luego 1 $/mes durante 3 meses; ver precio en EUR en tu panel).
3. Comprobar que la tienda está con contraseña: *Tienda online → Preferencias → Protección con contraseña* activada. Mensaje: "Muy pronto. Estamos preparando la primera colección."
4. Conectar el conector **Shopify** en claude.ai para que el chat Web pueda configurar la tienda directamente.
5. No conectar dominio todavía (pendiente de elegir variante).

## Fase 2 — Tema y diseño (chat Web)
**Tema:** Horizon (gratis). Instalar y personalizar en *Tienda online → Temas*.

**Ajustes del tema**
| ajuste | valor |
|---|---|
| Fondo | crema `#F7F3EC` |
| Fondo de secciones alternas | arena `#E8DCC8` |
| Texto | ébano `#2B2A28` |
| Botones y ofertas | terracota `#B4694A`, texto crema |
| Detalles (etiquetas, bordes suaves) | salvia `#A3B1A0` / azul bruma `#8FA3B0` |
| Títulos | Cormorant Garamond (si no está en la biblioteca de Shopify: la más parecida, p. ej. Cormorant) |
| Texto | Manrope |
| Esquinas | rectas o muy suaves (2-4 px) |
| Logo | `marca/logo/logo-color.svg` (exportar a PNG 600 px si el tema no acepta SVG) |
| Favicon | `marca/logo/icono.svg` → PNG 32×32 |

**Página de inicio (móvil primero)**
1. Barra de anuncio: "Envíos a toda Europa y Reino Unido" (confirmar con Operaciones).
2. Imagen principal + título corto ("Cae como debe.") + botón "Ver colección".
3. Bloque diferencia: "Elige tu largo: petite, regular o tall" + "Tejidos que no transparentan".
4. Colección destacada (vacía hasta la primera colección).
5. Guía de largos: enlace a la guía de tallas.
6. Suscripción al email ("Te avisamos del lanzamiento").

**Menús**
- Principal: Novedades · Abayas · Vestidos · Hiyabs · Guía de largos
- Pie: Envíos · Devoluciones · Guía de tallas · Contacto · Aviso legal · Privacidad · Cookies

## Fase 3 — Estructura vacía
- Colecciones: Novedades, Abayas, Vestidos, Hiyabs (provisional; las decide Producto).
- Variante de producto "Largo" (petite / regular / tall) además de "Talla": plantilla de producto preparada.
- Páginas: Sobre Nesma, Guía de tallas y largos, Contacto, FAQ.
- Políticas: generar borradores con la herramienta de Shopify; los textos finales los revisa Legal-finanzas.

## Fase 4 — Antes de abrir (más adelante)
Pagos (Shopify Payments), Markets (EU + UK, traducciones), envíos, impuestos (OSS), apps (reseñas, email), píxeles Meta/TikTok, dominio.

## Depende de otros chats
| tema | chat |
|---|---|
| Colecciones, tallas, precios, fichas | Producto |
| Envíos y devoluciones | Operaciones |
| Países, idiomas, IVA OSS | Mercados |
| Textos legales y políticas | Legal-finanzas |
| Fotos y vídeos | Contenido |
