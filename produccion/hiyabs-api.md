# Hiyabs elegidos con la API de AliExpress (10/10/2026)

Datos oficiales de la API Dropshipping de AliExpress (app *Nesma Sourcing*). Precios con IVA incluido. Mercados principales: **UK, FR, DE, NL, IT**.

## Hallazgo clave: envío *Choice* 1,99 € aunque el pedido lleve 1, 2 o 3 hiyabs
En los productos *Choice* el envío a los 5 países cuesta **1,99 € por pedido**, sea 1 o 3 unidades (comprobado con 3 ud. a Francia). En la UE el arancel es 3 € (+IVA ≈ 3,63 €) **por línea**: 3 hiyabs del mismo modelo en un paquete pagan un solo arancel. → **Packs muy rentables.**

Los productos que **no** son Choice (ej. set GELMOIN con gorro, 4,9★, 2.000+ ventas) cuestan 6-8,5 € de envío por pedido → descartados por coste.

## ¿Almacén en Europa?
No para estos hiyabs (10/10/2026): la API de envíos devuelve **"ship_from: CN"** para los 5 finalistas y los 5 países, y sus fichas no tienen opción "Enviar desde" europea. El filtro por almacén en la búsqueda de la API no funciona (devuelve los mismos productos), y en la app de AliExpress el filtro UE solo muestra revendedores a 31-67 € sin ventas. Con *Choice* desde China el plazo ya es de 4-13 días.

## Finalistas
| hiyab | tienda | ID AliExpress | ventas | nota | reseñas | colores | precio | coste 1 ud. UE | coste 1 ud. UK | pack 3 iguales UE (por ud.) | envío a | días | en Shopify |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Modal/rayón liso 190×85 | Hijab Glamour Store | 1005007100433982 | 1.000+ | 4.7 | 250 | 39 | 7.39-8.49 € | 14.11 € | 10.48 € | 10.36 € | GB,FR,NL,IT (DE: no disponible hoy) | 4-10 | 11262957683031 (VS527) |
| Jersey modal 170×60 | SANMAIHUA Official Store | 1005005178341043 | 900+ | 4.5 | 283 | 30 | 5.99-7.19 € | 12.81 € | 9.18 € | 9.06 € | los 5 | 5-11 | 11262959255895 (#8) |
| Crinkle rayón | Yiwu Vora scarf Store | 1005006645829730 | 480 | 4.8 | 65 | 62 | 8.69-9.99 € | 15.61 € | 11.98 € | 11.86 € | los 5 | 7-13 | 11262958010711 (#4) |
| Modal 170×60 | HAOYAN Store | 1005006319086970 | 254 | 4.7 | 145 | 24 | 6.19-6.99 € | 12.61 € | 8.98 € | 8.86 € | GB,FR,DE,IT (NL: error hoy) | 5-10 | — (nuevo) |
| Jersey algodón 170×60 | HAOYAN Store | 1005006919742077 | 600+ | 4.6 | 237 | 9 | 5.59-6.89 € | 12.51 € | 8.88 € | 8.76 € | GB,FR,DE,NL (IT: error hoy) | 3-11 | 11262957781335? (#1) |

*Coste 1 ud. UE* = precio más caro + 1,99 € envío + 3,63 € arancel. *UK* = sin arancel (IVA UK cobrado por AliExpress). La correspondencia con Shopify se ha hecho por título y precio; confirmar en DSers.

## Descartados con datos
- Set modal + gorro GELMOIN (1005009107242857): envío 6-8,5 € (no Choice).
- Jersey líquido premium GELMOIN (1005011722159135): envío 7-7,7 € y solo 128 ventas.
- Hiyab instantáneo jersey 2.000+ (1005007170752900): «todas las variantes no vendibles» hoy.
- Seda/satén cuadrados, gorros, chifón y gasa: no cumplen el filtro de opacidad o no son hiyab largo.

## Cómo repetir la consulta
`produccion/api/` + `.github/workflows/aliexpress-api.yml`: se escribe la consulta en `peticion.json`, GitHub la ejecuta y deja la respuesta en `resultado.json`.

## Estado en Shopify (10/10/2026, 06:15) — fuente de verdad
Revisado el **stock por color** con la API (≥100 ud. por color = disponible).

| en tienda (borrador, tipo Hiyab + novedad) | ID AliExpress | Shopify ID | colores con stock | nota |
|---|---|---|---|---|
| Crinkle de rayón (Vora) — **creado por Producción** | 1005006645829730 | 11263097733463 | 44 (incl. beige, gris, camello, café) | ✅ el más completo |
| Modal 170×60 (HAOYAN) | 1005006319086970 | 11262959223127 | 14 (crema, gris hielo, azul marino, café, blanco…) | ✅ |
| Jersey premium (Laven Official Store) | 1005008076898965 | 11262957846871 | 23 (beige, crema, gris claro, azul marino, camello…) | ✅ nota 4,4, 700+ ventas, Choice 1,99 € |
| Modal/rayón liso (Hijab Glamour) | 1005007100433982 | 11262957683031 | 10, sin negro ni beige | ⚠️ colores limitados |

**Descartados por stock:** jersey SANMAIHUA (1005005178341043) y jersey algodón HAOYAN (1005006919742077): los colores neutros tienen 0-20 ud.

**Archivados** (estado *Archivado*, etiqueta `descartado`, reversible): los otros 21 productos importados con DSers. Incluye los 7 ✅ de la selección v1 que no se han podido verificar con la API (sin ID de AliExpress conocido) y el crinkle VS723 duplicado.

**Pendiente:**
- El crinkle creado por Producción **no está enlazado en DSers**: antes de vender, en DSers → *Mapping* del producto, pegar `https://www.aliexpress.com/item/1005006645829730.html`. Los SKU de Shopify llevan el ID de variante de AliExpress (`AE-producto-sku`).
- Precio de venta = coste provisional; lo fija el chat **Producto**. El campo "coste por artículo" ya tiene el coste del proveedor.
- Faltan negro y blanco/crema en jersey con buen stock: buscar con la API.
