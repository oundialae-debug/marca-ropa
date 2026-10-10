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

## Búsqueda ampliada (10/10/2026, 06:30)
El catálogo de dropshipping de la API en la categoría hiyabs tiene ~240 productos (12 páginas). Revisados todos los hiyabs largos con ≥80 ventas y nota ≥4,5:
| producto | ID | resultado |
|---|---|---|
| Set hiyab modal + gorro (GELMOIN, 4,9★, 577 reseñas, 2.000+) | 1005009107242857 | ✅ **premium**: 66 colores con stock (beige, blanco, azul marino…), pero envío 6-8,5 € por pedido (no Choice). Para vender en packs o a precio alto. |
| Hiyab cobertura completa elástico (5,0★, 9 reseñas, 117) | 1005002864337827 | ⚠️ reserva: 16 colores con stock (incl. negro), envío 2,15-2,86 € pero hasta 17 días; pocas reseñas |
| Jersey líquido premium (GELMOIN) | 1005011722159135 | ❌ envío 7,7-10 € y no envía a UK |
| Algodón voile fino / rayón voile (2) | 1005006421100014, 1005011536840709 | ❌ tejido fino (riesgo de transparencia) |
| Gasa SANMAIHUA | 1005004710849831 | ❌ gasa |
| Instantáneos, gorros, jersey acanalado, pañuelo largo con lazo (6) | varios | ❌ sin stock |

**Conclusión:** con el catálogo de la API salen **6** (4 + set GELMOIN + reserva). Para llegar a 10-12: la usuaria pega enlaces de AliExpress que le gusten y Producción los verifica con la API al momento (stock por color, nota, envío).

## Lista final para importar (criterio relajado, 10/10/2026 06:45)
Decisión de la usuaria: aceptar modelos con pocas reseñas si la tienda es buena (nota de tienda ≥4,5) y cumplen tejido opaco + stock en neutros + envío Choice 1,99 €.

| orden | hiyab | tienda (nota) | ID AliExpress | nota producto | colores con stock (neutros) | precio | envío | estado |
|---|---|---|---|---|---|---|---|---|
| — | Modal 170×60 | HAOYAN | 1005006319086970 | 4,7 (145) | 14 | 6,19-6,99 € | 1,99 € (NL error hoy) | ya en tienda |
| — | Jersey premium | Laven Official (4,4) | 1005008076898965 | 4,4 (183) | 23 | 4,89-5,99 € | 1,99 € | ya en tienda |
| — | Modal/rayón liso | Hijab Glamour (4,5) | 1005007100433982 | 4,7 (250) | 10 (5) | 7,99-8,99 € | 1,99 € (DE no) | ya en tienda ⚠️ |
| 1 | Crinkle rayón | Yiwu Vora (4,6) | 1005006645829730 | 4,8 (65) | 44 (14) | 8,79-10,59 € | 1,99 € | importar (sustituye la copia creada a mano) |
| 2 | Crinkle algodón grande | RUNMEIFA Official (4,7) | 1005006411486233 | 4,5 (11) | 54 (20) | 4,49-4,89 € | 1,99 € los 5 países | importar |
| 3 | Algodón liso (sarga) | RUNMEIFA Official (4,7) | 33055642968 | 4,8 (27) | 22 (11) | 4,59-5,49 € | 1,99 € (UK/NL error hoy) | importar |
| 4 | Jersey liso | SANMAIHUA Hijab Store (4,7) | 4000022442764 | 5,0 (3) | 30 (11) | 6,39-8,19 € | 1,99 € | importar |
| 5 | Jersey arrugado algodón | SANMAIHUA Official (4,7) | 1005005633125258 | 4,3 (4) | 18 (11) | 5,29-5,59 € | 1,99 € (DE no) | importar |
| 6 | Hiyab instantáneo algodón | Forever Scarf (4,7) | 1005008208535051 | 4,7 (29) | 10 (6) | 7,29-7,89 € | 1,99 € | importar |
| 7 | Set hiyab modal + gorro (premium) | GELMOIN (4,9) | 1005009107242857 | 4,9 (577) | 66 | 7,99 € | 6-8,5 € (no Choice) | importar |
| 8 | Cobertura completa elástico (reserva) | Islamic products | 1005002864337827 | 5,0 (9) | 16 (10, incl. negro) | 4,29 € | 2,15-2,86 €, hasta 17 días | importar como reserva |

Total: 3 en tienda + 8 por importar = **11**. RUNMEIFA (2 modelos) permite pedidos combinados de la misma tienda.

## Corrección (10/10/2026 06:40)
Comparadas las fotos de AliExpress (API) con todos los productos de Shopify, incluidos los archivados:
- Crinkle Vora 1005006645829730 = **11262958010711** (importado con DSers, se había archivado por error) → recuperado. La copia creada a mano (11263097733463) queda archivada con etiqueta `copia-manual`.
- Jersey liso 4000022442764 = **11262958141783** (primer hiyab importado, archivado por error) → recuperado.
- **En tienda (borrador, Hiyab + novedad, enlazados en DSers): 5** → 11262958010711, 11262958141783, 11262959223127, 11262957846871, 11262957683031.
- **Por importar: 6** → 1005006411486233, 33055642968, 1005005633125258, 1005008208535051, 1005009107242857, 1005002864337827.
