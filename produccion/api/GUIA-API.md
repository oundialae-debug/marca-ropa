# Guía de la API de AliExpress para Nesma (Producción)

App **Nesma Sourcing** (tipo Dropshipping individual, App Key 552384) en la AliExpress Open Platform. Documentación oficial descargada en `docs/` (16 APIs de la sección AE-Dropshipper; resumen legible en `docs/RESUMEN_dropshipper.md`).

## Cómo se usa
1. Producción escribe las llamadas en `peticion.json` (lista `llamadas`).
2. Al subirlo, GitHub Actions (`.github/workflows/aliexpress-api.yml`) ejecuta `ae_call.py`: firma (HMAC-SHA256), añade el token y llama a `api-sg.aliexpress.com`.
3. La respuesta queda en `resultado.json`. El token se guarda cifrado en `token.enc` y se renueva solo (`/auth/token/refresh`) cuando le quedan <6 h.
4. La App Secret vive solo como secreto de GitHub (`AE_APP_SECRET`). **Regenerarla** en AliExpress porque se compartió por chat, y actualizar el secreto.
- Si caduca la autorización (refresh token caducado): abrir `https://api-sg.aliexpress.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://nzwtqv-su.myshopify.com&client_id=552384`, copiar el `code` y canjearlo con una llamada `{"tipo":"token","code":"..."}` (caduca en 3 min).

## Qué ofrece (sección AE-Dropshipper) y para qué nos sirve
| API | qué hace | uso en Nesma |
|---|---|---|
| `aliexpress.ds.text.search` | búsqueda por texto en el catálogo DS; filtros `categoryId`, `sortBy` (`orders,desc`, `min_price,asc`, `comments,desc`…), `searchExtend`, `selectionName` | ✅ usado. Catálogo limitado (~240 hiyabs en la categoría 200003922) |
| `aliexpress.ds.image.searchV2` | **búsqueda por imagen** (`same`/`similar`), ordena por ventas o precio, devuelve `ship_from`, ventas, valoración, precio | ✅ probado: encuentra productos que el texto no muestra. **La mejor vía para ampliar catálogo** y buscar el mismo producto en otras tiendas |
| `aliexpress.ds.product.get` | ficha completa: SKUs, **stock por color**, precio con IVA, tienda y nota, propiedades (material/tela), peso, `wholesale_price_tiers`, impuestos estimados | ✅ usado (filtro de stock y tejido) |
| `aliexpress.ds.freight.query` | envío real por país y cantidad: coste, días, `ship_from_country`, `free_shipping_threshold`, `ddpIncludeVATTax`, `available_stock`, código del servicio | ✅ usado. `DELIVERY_SERVICE_EXCEPTION` es un fallo puntual; `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS` es bloqueo real |
| `aliexpress.ds.feed.itemids.get` | listas de IDs por `feed_name` (selecciones de AliExpress) | por probar: otra vía de descubrir productos |
| `aliexpress.ds.category.get` / `category.tree.get` | árbol de categorías (hiyabs = 200003922) | ✅ |
| `aliexpress.ds.product.wholesale.get` | precios por volumen (modelo mayorista) | fase 2 / compras de stock |
| `aliexpress.ds.member.benefit.get` | beneficios de la cuenta DS | ✅ la cuenta **puede solicitar `wholesale-benefit`** (precios de mayorista) → decidir en chat General |
| `aliexpress.ds.product.specialinfo.get` | certificados del producto por país | para Legal-finanzas (cumplimiento UE) |
| `aliexpress.ds.order.create` / `order.afterpay` | crear y pagar pedidos | ⛔ **no usar sin permiso de la usuaria** (compras reales). Hoy lo hace DSers |
| `aliexpress.trade.ds.order.get` / `ds.order.tracking.get` | estado del pedido y seguimiento | para Operaciones cuando haya pedidos |
| `aliexpress.logistics.buyer.freight.calculate` | cálculo de envío antiguo | usar `ds.freight.query` |
| `aliexpress.ds.search.event.report` | informe de eventos de búsqueda a AliExpress | no necesario |

## Lecciones
- La búsqueda por texto y por imagen devuelven precios en céntimos o con IVA según el campo: usar `product.get` para el precio real.
- Para Choice, el envío es 1,99 € por pedido aunque lleve varias unidades del mismo anuncio.
- Comprobar siempre el **título completo** (los títulos en español a veces esconden que es un gorro interior).
- Antes de archivar o importar, cruzar fotos de AliExpress con Shopify para saber qué anuncio es cada producto.
