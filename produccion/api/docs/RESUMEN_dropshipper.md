# Documentación oficial AliExpress — sección AE-Dropshipper

Descargada el 10/10/2026 del servicio de documentación de openservice.aliexpress.com (cid 21038). JSON completos en esta carpeta.

**Parámetros comunes a todas:** `app_key`, `timestamp` (ms, <7200 s de diferencia con UTC), `sign_method`, `sign`, `access_token` (opcional según API).


---
## `aliexpress.ds.category.get` — API for fetch AE Category's ID and Category Name

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2023-06-19 12:23:38

**Parámetros:**
- `categoryId` (String): categoryId
- `language` (String): language:hi de ru pt ko in en it fr zh es iw ar vi th uk ja id pl he nl tr
- `app_signature` (String): signature

**Respuesta (resumen):**
- `resp_result` (Object): Respond result
  - `resp_code` (Number): Respond status code
  - `resp_msg` (String): Description of the respond status code
  - `result` (Object): Detail of the respond
    - `categories` (Object[]): category
      - `category_id` (Number): Category ID
      - `category_name` (String): Category Name
      - `parent_category_id` (Number): Parent category ID
    - `total_result_count` (Number): Respond result count

**Errores:** `UnsupportedParamMapping`: Unsupported parameters, please check the parameters

---
## `aliexpress.ds.category.tree.get` — AE DS Category Tree Get

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2026-07-07 19:27:48

**Parámetros:**
- `lang` (String) **obligatorio**: language

**Respuesta (resumen):**
- `rsp_code` (Number): response code
- `rsp_msg` (String): response message
- `result` (String): result

---
## `aliexpress.ds.feed.itemids.get` — Fetch items with feedname in simple model

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-07-18 14:21:30

**Parámetros:**
- `page_size` (Number): number of each page
- `category_id` (String): first level category id, you can get from category query
- `feed_name` (String) **obligatorio**: query api ‘aliexpress.ds.feedname.get’
- `search_id` (String): 

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: result object
  - `products` (Number[]) **obligatorio**: item id list
  - `search_id` (String): search id, put it in the next request. Only valid in 1 minutes
  - `total` (Number): total item id left
- `rsp_msg` (String) **obligatorio**: result msg
- `rsp_code` (Number) **obligatorio**: result code
- `ret` (Boolean): true is success, false for fail

---
## `aliexpress.ds.freight.query` — Delivery/Freight API

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-03-04 20:23:41

**Parámetros:**
- `queryDeliveryReq` (Object) **obligatorio**: delivery query request
  - `quantity` (Number) **obligatorio**: quantity for your request
  - `shipToCountry` (String) **obligatorio**: country that ships to
  - `productId` (String) **obligatorio**: product_id
  - `provinceCode` (String): The province code, used to query shipping fees for local-to-local products. Please provide either province or provinceCode; do not provide both.
  - `cityCode` (String): The city code. Optional.
  - `language` (String) **obligatorio**: language
  - `locale` (String) **obligatorio**: locale
  - `selectedSkuId` (String) **obligatorio**: selected sku
  - `currency` (String) **obligatorio**: currency for calculate the freight fee
  - `province` (String): The province name, used to query shipping fees for local-to-local products. Please provide either province or provinceCode; do not provide both.

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: result
  - `msg` (String) **obligatorio**: error msg
  - `delivery_options` (Object[]) **obligatorio**: list of deliveryOptions
    - `shipping_fee_format` (String) **obligatorio**: format String shipping fee to make it understandable
    - `delivery_date_desc` (String) **obligatorio**: format delivery date estimation
    - `code` (String) **obligatorio**: delivery service code, which is used for place order
    - `free_shipping` (Boolean) **obligatorio**: true means free, false means not free
    - `max_delivery_days` (Number) **obligatorio**: estimated delivery days, max days
    - `estimated_delivery_time` (String) **obligatorio**: delivery estimation
    - `min_delivery_days` (Number) **obligatorio**: estimated delivery days, main days
    - `shipping_fee_currency` (String) **obligatorio**: shipping fee currency
    - `ship_from_country` (String) **obligatorio**: where your sku will ship from
    - `company` (String) **obligatorio**: shipping service company name which you can use to display
    - `shipping_fee_cent` (String) **obligatorio**: shipping fee amount in cent
    - `tracking` (Boolean): is this shipping option can be tracking
    - `mayHavePFS` (Boolean): if it can be platFormFreeShipping
    - `available_stock` (String): available stock for sku
    - `guaranteed_delivery_days` (String): it is a guaranteed days
    - `ddpIncludeVATTax` (String): if price include ddp vat tax
    - `free_shipping_threshold` (String): free shipping threshold
  - `code` (Number) **obligatorio**: status of this request: 200 means success
  - `success` (Boolean) **obligatorio**: true means it is success

**Errores:** `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS`: Logistics cannot be delivered to the specified address; `DELIVERY_INFO_EMPTY`: The product ID is wrong, please check the product ID

---
## `aliexpress.ds.image.searchV2` — ae dropshiper image search v2

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-12-04 19:26:33

**Parámetros:**
- `param0` (Object): param0
  - `search_type` (String): image search type(same/similar)
  - `image_base64` (String): image encoded using base64
  - `currency` (String): currency
  - `lang` (String): language
  - `sort_type` (String): sort type(price/orders)
  - `sort_order` (String): sort order(asc/desc)
  - `ship_to` (String): ship to country

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: result
  - `messages` (String) **obligatorio**: message
  - `empty` (Boolean) **obligatorio**: empty
  - `ret` (Boolean) **obligatorio**: ret
  - `code` (String) **obligatorio**: code
  - `data` (Object[]) **obligatorio**: data
    - `product_main_image_url` (String) **obligatorio**: product_main_image_url
    - `target_original_price_currency` (String) **obligatorio**: target_original_price_currency
    - `evaluate_rate` (String) **obligatorio**: evaluate_rate
    - `target_original_price` (String) **obligatorio**: target_original_price
    - `shop_id` (Number) **obligatorio**: shop_id
    - `second_level_category_title` (String) **obligatorio**: second_level_category_title
    - `ship_from` (String): US
    - `similarity_score` (String): similarity score
    - `first_level_category_id` (String) **obligatorio**: first_level_category_id
    - `product_id` (String) **obligatorio**: product_id
    - `target_sale_price_currency` (String) **obligatorio**: target_sale_price_currency
    - `discount` (String) **obligatorio**: discount
    - `second_level_category_id` (String) **obligatorio**: second_level_category_id
    - `latest_volume` (String) **obligatorio**: latest_volume
    - `product_title` (String) **obligatorio**: product_title
    - `product_detail_url` (String) **obligatorio**: product_detail_url
    - `first_level_category_title` (String) **obligatorio**: first_level_category_title
    - `target_sale_price` (String) **obligatorio**: target_sale_price

---
## `aliexpress.ds.member.benefit.get` — ds member benefit get

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-08-27 20:40:05

**Parámetros:**
- (ninguno aparte de los comunes)

**Respuesta (resumen):**
- `rsp_msg` (String): rsp_msg
- `rsp_code` (String): rsp_code
- `result` (Object[]): result
  - `code` (String): benefit code
  - `title` (String): benefit title
  - `canApply` (String): flag if can apply the benefit
  - `canBenefit` (String): flag if already own the benefit

---
## `aliexpress.ds.order.afterpay` — AE DS Order After Pay API

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2026-07-03 15:13:09

**Parámetros:**
- `req` (Object) **obligatorio**: 订单id
  - `order_id` (String) **obligatorio**: 订单id

**Respuesta (resumen):**
- `rsp_msg` (String): 响应信息
- `rsp_code` (String): 响应码
- `result` (Boolean): 是否响应成功

---
## `aliexpress.ds.order.create` — AE DS Order Create and Pay API

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-04-29 13:36:13

**Parámetros:**
- `ds_extend_request` (Object): DS ExtendParam
  - `promotion` (Object): promotionCode
    - `promotion_channel_info` (String): promotionChannelInfo
    - `promotion_activity_id` (String): promotion id from coupon query API's field "dsCouponId"
  - `payment` (Object): {"payment":{"pay_currency":"xxx"}}
    - `pay_currency` (String): USD
    - `try_to_pay` (String): Please auth your account as DS Before set it true
  - `trade_extra_param` (Object): whether it is wholesale
    - `business_model` (String): "wholesale" for wholesale model, "retail" for retail model, default for retail model
    - `customize_sku_map` (Object): key is sku_id, value is customize_id
    - `nat_addr` (String): SA natAddr
    - `birthday` (String): Recipient's Birthday. This field is mandatory if the destination country is Brazil (BR). Format: ddMMyyyy (Day-Month-Year, 8 digits, no separators). Example: 01022026 represents February 1st, 2026.
  - `channel_strategy` (String): channel_strategy
- `param_place_order_request4_open_api_d_t_o` (Object) **obligatorio**: specific order parameters
  - `out_order_id` (String): outer order id, used for idempotent checkout
  - `logistics_address` (Object) **obligatorio**: logistic address information
    - `address` (String) **obligatorio**: address information
    - `address2` (String): address extension information
    - `city` (String) **obligatorio**: city
    - `contact_person` (String): contact person
    - `country` (String) **obligatorio**: receiver country
    - `cpf` (String): taxpayer identification number
    - `full_name` (String): receiver full name
    - `locale` (String): internationalization locale
    - `mobile_no` (String): mobile phone number
    - `passport_no` (String): passport number
    - `passport_no_date` (String): passport expiry date
    - `passport_organization` (String): passport issuing agency
    - `phone_country` (String): country code of the phone
    - `province` (String) **obligatorio**: province
    - `tax_number` (String): tax number
    - `zip` (String): zip code
    - `rut_no` (String): Chile tax number (not used)
    - `foreigner_passport_no` (String): foreign tax number (registration card number or passport number is required for Korean foreigners)
    - `is_foreigner` (String): whether it is a foreigner
    - `vat_no` (String): vat tax number
    - `tax_company` (String): company name
    - `location_tree_address_id` (String): location tree address id
  - `product_items` (Object[]) **obligatorio**: product attributes
    - `product_count` (Number) **obligatorio**: product count
    - `product_id` (Number) **obligatorio**: product id
    - `sku_attr` (String): product sku
    - `logistics_service_name` (String): logistics service name
    - `order_memo` (String): user Comments

**Respuesta (resumen):**
- `result` (Object): result
  - `error_code` (String): errorCode
  - `error_msg` (String): errorMsg
  - `order_list` (Number[]): orderList
  - `is_success` (Boolean): success

**Errores:** `B_DROPSHIPPER_DELIVERY_ADDRESS_VALIDATE_FAIL`: The address is wrong, please check the address; `B_DROPSHIPPER_DELIVERY_ADDRESS_CPF_CN_INVALID`: CPF error, please check CPF; `B_DROPSHIPPER_DELIVERY_ADDRESS_CPF_NOT_MATCH`: CPF error, please check CPF; `BLACKLIST_BUYER_IN_LIST`: The user ID status is abnormal. Please try to change the user to place the order.; `USER_ACCOUNT_DISABLED`: The user ID status is abnormal. Please try to change the user to place the order.; `PRICE_PAY_CURRENCY_ERROR`: Products should declare as same currency.; `DELIVERY_METHOD_NOT_EXIST`: Please fill valid delivery method (You can use se aliexpress.freight.query check it); `INVENTORY_HOLD_ERROR`: Inventory is insufficient or system error occured.

---
## `aliexpress.ds.order.tracking.get` — Ds Order Tracking

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-07-09 18:01:56

**Parámetros:**
- `ae_order_id` (String) **obligatorio**: Order ID which you get from order.create
- `language` (String) **obligatorio**: language

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: result
  - `ret` (Boolean) **obligatorio**: true for success
  - `code` (String) **obligatorio**: error code
  - `data` (Object) **obligatorio**: tracking list dto
    - `tracking_detail_line_list` (Object[]) **obligatorio**: tracking list
      - `mail_no` (String) **obligatorio**: mail number
      - `detail_node_list` (Object[]) **obligatorio**: tracking node
        - `tracking_name` (String) **obligatorio**: tracking node description
        - `time_stamp` (Number) **obligatorio**: timestamp
        - `tracking_detail_desc` (String) **obligatorio**: tracking node description
      - `carrier_name` (String) **obligatorio**: carrier name
      - `eta_time_stamps` (Number) **obligatorio**: timestamp
      - `package_item_list` (Object[]) **obligatorio**: package item
        - `item_id` (Number) **obligatorio**: item id
        - `quantity` (Number) **obligatorio**: count
        - `item_title` (String) **obligatorio**: item title
        - `sku_desc` (String) **obligatorio**: sku desc
        - `sku_id` (Number): sku id
      - `cp_name` (String): carrier partner name
      - `cp_website_url` (String): carrier partner website url
  - `msg` (String) **obligatorio**: error message

**Errores:** `UnsupportedParamMapping`: Parameter error, please check the parameters; `TRACKING DATA NOT FOUND`: The logistics number is wrong, please check the logistics number

---
## `aliexpress.ds.product.get` — product info query for ds

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2026-10-10 12:52:32

**Parámetros:**
- `ship_to_country` (String) **obligatorio**: Country
- `product_id` (Number) **obligatorio**: Item ID
- `target_currency` (String): Target currency
- `target_language` (String): hi de ru pt ko in en it fr zh es iw ar vi th uk ja id pl he nl tr (lowercase) or "en_US"、"ko_KR"...
- `remove_personal_benefit` (Boolean): if true, you will not get any crowd type promotion
- `biz_model` (String): BETA version for open api business model
- `province_code` (String): provice
- `city_code` (String): city

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: Product search results
  - `logistics_info_dto` (Object) **obligatorio**: Logistics information
    - `ship_to_country` (String) **obligatorio**: Country
    - `delivery_time` (Number) **obligatorio**: Goods lead time
  - `ae_item_base_info_dto` (Object) **obligatorio**: Basic commodity information
    - `gmt_modified` (String) **obligatorio**: Item Updated Time
    - `product_id` (Number) **obligatorio**: Item ID
    - `subject` (String) **obligatorio**: The title of the product
    - `product_status_type` (String) **obligatorio**: Product status
    - `gmt_create` (String) **obligatorio**: Commodity creation time
    - `mobile_detail` (String) **obligatorio**: Mobile detailed description
    - `avg_evaluation_rating` (String) **obligatorio**: Average rating stars, 1-5 stars
    - `evaluation_count` (String) **obligatorio**: Evaluation number
    - `owner_member_seq_long` (Number) **obligatorio**: Seller's master account ID
    - `detail` (String) **obligatorio**: Commodity detailed description
    - `currency_code` (String) **obligatorio**: The currency unit of the commodity. U.S. Dollar: USD, Ruble: RUB
    - `category_id` (Number) **obligatorio**: ID of the category of the product
    - `sales_count` (String): Sales volume of product
    - `category_sequence` (String): category sequence
    - `separated_listing` (Boolean): is separated per sku
    - `sl_product` (Boolean): is super link product
    - `sl_related_product_id` (Number): super link product id
  - `ae_item_properties` (Object[]) **obligatorio**: Attribute information
    - `attr_value_start` (String) **obligatorio**: Interval attribute start value
    - `attr_value_id` (Number) **obligatorio**: Attribute ID
    - `attr_value_end` (String) **obligatorio**: End value of interval attribute
    - `attr_value` (String) **obligatorio**: Attribute value
    - `attr_value_unit` (String) **obligatorio**: Attribute unit
    - `attr_name` (String) **obligatorio**: Attribute name
    - `attr_name_id` (Number) **obligatorio**: Attribute ID
  - `ae_item_sku_info_dtos` (Object[]) **obligatorio**: SKU information
    - `offer_bulk_sale_price` (String) **obligatorio**: SKU bulk discount price
    - `sku_available_stock` (Number) **obligatorio**: SKU inventory
    - `sku_bulk_order` (Number) **obligatorio**: Minimum number of batches
    - `sku_price` (String) **obligatorio**: Origin SKU price. Value range: 0.01-100000; Unit: USD. Such as: 200.07, which means: 200 US dollars 7 points. Need to be in the correct price range.
    - `offer_sale_price` (String) **obligatorio**: SKU discount price
    - `id` (String) **obligatorio**: sku attribute unique key
    - `ae_sku_property_dtos` (Object[]) **obligatorio**: SKU attribute object
      - `sku_property_value` (String) **obligatorio**: Attribute value
      - `property_value_id` (Number) **obligatorio**: Custom id
      - `sku_property_name` (String) **obligatorio**: Attribute name
      - `sku_property_id` (Number) **obligatorio**: Attribute ID
      - `property_value_definition_name` (String) **obligatorio**: Custom name
      - `sku_image` (String) **obligatorio**: SKU pictures
    - `barcode` (String) **obligatorio**: Commodity barcode
    - `currency_code` (String) **obligatorio**: The currency unit of the product. U.S. Dollar: USD, Ruble: RUB
    - `sku_id` (String): sku id, can be used for aliexpress.logistics.buyer.freight.calculate request
    - `sku_attr` (String): sku attribute unique key in new field name
    - `ean_code` (String): eanCode
    - `price_include_tax` (Boolean): if the price include tax
    - `wholesale_price_tiers` (Object[]): display when the item has wholesale price
      - `min_quantity` (String): threshold quantity for wholesale
      - `discount` (String): discount rate
      - `wholesale_price` (String): whole price
    - `buy_amount_limit_set_by_promotion` (String): promotion buy limit
    - `limit_strategy` (String): the limit strategy after you reach promotion limit
    - `tax_currency_code` (String): currency code of tax
    - `tax_amount` (String): tax amount
    - `estimated_import_charges` (String): Products from the People's Republic of China (which include products from Hong Kong) entering the U.S. for consumption will be subject to all applicable import charges (duties, taxes, fees, exactions, etc.) according to the currently effective regulatory requirements in the U.S. To ensure compliance
    - `channel_discount_price` (String): ds channel price
- … (38 campos más en el JSON)

**Errores:** `Item is not allowed to this country`: The product is prohibited from sale in this country. Please change the country or product.; `ITEM_ID_NOT_FOUND`: The product itemid is wrong, please check the itemid; `System Error`: System error,Need to contact technical support

---
## `aliexpress.ds.product.specialinfo.get` — get products' special info like certification

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2023-11-22 07:06:25

**Parámetros:**
- `itemId` (Number) **obligatorio**: product id
- `countryCodes` (String[]) **obligatorio**: country code
- `appKey` (String) **obligatorio**: your appkey

**Respuesta (resumen):**
- `result` (Object) **obligatorio**: result
  - `ret` (Boolean) **obligatorio**: bool to tag if it is success
  - `code` (String) **obligatorio**: error code
  - `data` (Object) **obligatorio**: data_demo
    - `product_id` (String) **obligatorio**: productId
    - `item_qualification_list` (Object[]) **obligatorio**: item certification list
      - `value_type` (String) **obligatorio**: certification type
      - `name` (String) **obligatorio**: certification name
      - `value` (String) **obligatorio**: certification url
      - `key` (String) **obligatorio**: certification key
  - `err_message` (String) **obligatorio**: error message

---
## `aliexpress.ds.product.wholesale.get` — product info for whole sale business

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-12-05 21:32:41

**Parámetros:**
- `ship_to_country` (String) **obligatorio**: Country
- `product_id` (Number) **obligatorio**: Item ID
- `target_currency` (String): Target currency
- `target_language` (String): hi de ru pt ko in en it fr zh es iw ar vi th uk ja id pl he nl tr (lowercase) or "en_US"、"ko_KR"...
- `remove_personal_benefit` (Boolean): if true, you will not get any crowd type promotion

**Respuesta (resumen):**
- `rsp_msg` (String) **obligatorio**: result message
- `rsp_code` (Number) **obligatorio**: result code
- `result` (Object) **obligatorio**: Product search results
  - `ae_multimedia_info_dto` (Object) **obligatorio**: Multimedia information
    - `ae_video_dtos` (Object[]) **obligatorio**: Video information
      - `poster_url` (String) **obligatorio**: The URL of the video cover image
      - `media_status` (String) **obligatorio**: Video status
      - `ali_member_id` (Number) **obligatorio**: Seller's master account ID
      - `media_type` (String) **obligatorio**: Type of video
      - `media_id` (Number) **obligatorio**: Video ID
      - `media_url` (String): media url
    - `image_urls` (String) **obligatorio**: List of main images of the product
  - `package_info_dto` (Object) **obligatorio**: Package information
    - `base_unit` (Number) **obligatorio**: Number of basic products for custom weighing
    - `package_height` (Number) **obligatorio**: Product height
    - `gross_weight` (String) **obligatorio**: The gross weight of the product
    - `package_length` (Number) **obligatorio**: The length of the product
    - `package_width` (Number) **obligatorio**: Product width
    - `product_unit` (Number) **obligatorio**: Unit of commodity
    - `package_type` (Boolean) **obligatorio**: Type of packaging
  - `ae_store_info` (Object) **obligatorio**: Store Information
    - `item_as_described_rating` (String) **obligatorio**: Product description, 1-5 stars
    - `communication_rating` (String) **obligatorio**: Seller service, 1-5 stars
    - `shipping_speed_rating` (String) **obligatorio**: Logistics, 1-5 stars
    - `store_name` (String) **obligatorio**: Shop name
    - `store_id` (Number) **obligatorio**: Store ID
    - `store_country_code` (String): store country code, can be used as 'ship from' country of the sku
  - `product_id_converter_result` (Object): product id converter result
    - `main_product_id` (Number): main productId
    - `sub_product_id` (Object): sub productId
  - `has_whole_sale` (Boolean): has wholesale price
  - `logistics_info_dto` (Object) **obligatorio**: Logistics information
    - `ship_to_country` (String) **obligatorio**: Goods lead time
    - `delivery_time` (Number) **obligatorio**: Country
  - `ae_item_base_info_dto` (Object) **obligatorio**: Basic commodity information
    - `gmt_modified` (String) **obligatorio**: Item Updated Time
    - `product_id` (Number) **obligatorio**: Item ID
    - `subject` (String) **obligatorio**: The title of the product
    - `product_status_type` (String) **obligatorio**: Product status
    - `gmt_create` (String) **obligatorio**: Commodity creation time
    - `mobile_detail` (String) **obligatorio**: Mobile detailed description
    - `avg_evaluation_rating` (String) **obligatorio**: Average rating stars, 1-5 stars
    - `ws_display` (String) **obligatorio**: Reasons for removal of goods
    - `evaluation_count` (String) **obligatorio**: Evaluation number
    - `ws_offline_date` (String) **obligatorio**: The date the product was removed from the shelf
    - `owner_member_seq_long` (Number) **obligatorio**: Seller's master account ID
    - `detail` (String) **obligatorio**: Commodity detailed description
    - `currency_code` (String) **obligatorio**: The currency unit of the commodity. U.S. Dollar: USD, Ruble: RUB
    - `category_id` (Number) **obligatorio**: ID of the category of the product
    - `sales_count` (String): Sales volume of product
    - `category_sequence` (String): category sequence
  - `ae_item_properties` (Object[]) **obligatorio**: Attribute information
    - `attr_value_start` (String) **obligatorio**: Interval attribute start value
    - `attr_value_id` (Number) **obligatorio**: Attribute ID
    - `attr_value_end` (String) **obligatorio**: End value of interval attribute
    - `attr_value` (String) **obligatorio**: Attribute value
    - `attr_value_unit` (String) **obligatorio**: Attribute unit
    - `attr_name` (String) **obligatorio**: Attribute name
    - `attr_name_id` (Number) **obligatorio**: Attribute ID
  - `ae_item_sku_info_dtos` (Object[]) **obligatorio**: SKU information
- … (28 campos más en el JSON)

**Errores:** `All SKU Unsaleable`: The item is not available for sale, please exchange it.; `ITEM_ID_NOT_FOUND`: Product not found, please check product ID

---
## `aliexpress.ds.search.event.report` — search event report

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-11-05 15:54:36

**Parámetros:**
- `report_text` (String) **obligatorio**: out site event, for business analysis

**Respuesta (resumen):**
- `code` (String): code
- `msg` (String): msg
- `data` (String): data

---
## `aliexpress.ds.text.search` — text search for ds

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2024-08-29 16:54:29

**Parámetros:**
- `keyWord` (String): query word
- `local` (String) **obligatorio**: lang: en_US
- `countryCode` (String) **obligatorio**: ship to country
- `categoryId` (Number): categoryId
- `sortBy` (String): accept value: min_price,asc min_price,desc orders,asc orders,desc comments,asc comments,desc
- `pageSize` (Number): page size
- `pageIndex` (Number): page index
- `currency` (String) **obligatorio**: currency
- `searchExtend` (Object[]): search extend
  - `searchKey` (String): search key
  - `searchValue` (String): search value
  - `max` (String): max
  - `min` (String): min
- `selectionName` (String): text search within specific selection

**Respuesta (resumen):**
- `code` (String): code
- `msg` (String): message
- `data` (Object): data
  - `totalCount` (Number): total
  - `pageIndex` (Number): page index
  - `pageSize` (Number): page size
  - `products` (Object[]): products
    - `salePriceFormat` (String): sale price
    - `itemUrl` (String): item url
    - `orders` (String): orders
    - `score` (String): score
    - `title` (String): title
    - `itemMainPic` (String): item main picture url
    - `cateId` (String): cateId
    - `originalPriceFormat` (String): original price formated
    - `originMinPrice` (String): originMinPrice
    - `itemId` (String): itemId
    - `originalPrice` (String): originalPrice
    - `originalPriceCurrency` (String): originalPriceCurrency
    - `salePrice` (String): salePrice
    - `salePriceCurrency` (String): salePriceCurrency
    - `targetOriginalPrice` (String): targetOriginalPrice
    - `targetOriginalPriceCurrency` (String): targetOriginalPriceCurrency
    - `targetSalePrice` (String): targetSalePrice
    - `discount` (String): discount
    - `productVideoUrl` (String): product video url
    - `evaluateRate` (String): evaluateRate
    - `type` (String): "search" for search result, "recommend" for smart recommend engine result

**Errores:** `IllegalAccessToken`: AccessToken error, please check the accessToken

---
## `aliexpress.logistics.buyer.freight.calculate` — Freight calculation interface provided for buyers

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2022-03-30 15:44:05

**Parámetros:**
- `param_aeop_freight_calculate_for_buyer_d_t_o` (Object) **obligatorio**: Shipping Calculation Request Parameters
  - `sku_id` (String): skuId must be passed when calculating the choice product
  - `city_code` (String): city code
  - `country_code` (String) **obligatorio**: country code
  - `product_id` (Number) **obligatorio**: Product ID
  - `product_num` (Number) **obligatorio**: Product count
  - `province_code` (String): Province code
  - `send_goods_country_code` (String) **obligatorio**: Shipping country
  - `price` (String): commodity price
  - `price_currency` (String): commodity price currency

**Respuesta (resumen):**
- `result` (Object): result
  - `aeop_freight_calculate_result_for_buyer_d_t_o_list` (Object[]): aeopFreightCalculateResultForBuyerDTOList
    - `tracking_available` (String): tracking available
    - `error_code` (Number): errorCode
    - `estimated_delivery_time` (String): Estimated delivery time
    - `freight` (Object): freight
      - `amount` (String): amount
      - `cent` (Number): cent
      - `currency_code` (String): currencyCode
    - `service_name` (String): serviceName
  - `error_desc` (String): errorDesc
  - `success` (Boolean): success

---
## `aliexpress.trade.ds.order.get` — buyer query order details

{'data': [], 'id': None}

*Cobro:* no · *Actualizada:* 2022-03-30 15:43:59

**Parámetros:**
- `single_order_query` (Object) **obligatorio**: order query conditions
  - `order_id` (Number) **obligatorio**: order id

**Respuesta (resumen):**
- `result` (Object): order information
  - `user_order_amount` (Object): order amount in user's pay currency
    - `amount` (String): amount
    - `currency_code` (String): currency
  - `pay_timeout_second` (String): seconds for pay expiration, from order created
  - `order_paidtime_string` (String): order paid time
  - `gmt_create` (String): order creation time
  - `order_status` (String): order status
  - `logistics_status` (String): logistics status
  - `order_amount` (Object): order amount
    - `amount` (String): amount
    - `currency_code` (String): currency code
  - `child_order_list` (Object[]): child order list
    - `actual_tax_fee` (Object): tax amount in user's pay currency
      - `amount` (String): amount
      - `currency_code` (String): USD
    - `actual_shipping_fee` (Object): actual shipping fee = shippingfee - shippingdiscount
      - `amount` (String): fee amount
      - `currency_code` (String): currency
    - `already_include_tax` (String): does the product fee already include tax
    - `shipping_fee` (Object): shipping fee
      - `amount` (String): amount
      - `currency_code` (String): currency
    - `sale_discount_fee` (Object): sale discount
      - `amount` (String): amount
      - `currency_code` (String): currency
    - `sale_fee` (Object): sale fee
      - `amount` (String): amount
      - `currency_code` (String): currency
    - `actual_fee` (Object): actual fee = sale fee - sale discount + actual shipping
      - `amount` (String): amount
      - `currency_code` (String): currency
    - `shipping_discount_fee` (Object): shipping discount
      - `amount` (String): amount
      - `currency_code` (String): currency
    - `end_reason` (String): order's end reason CANCELED
    - `sku_id` (String): SKU id
    - `price_include_tax` (String): if price include tax
    - `end_reason_desc` (String): description of end reason
    - `product_id` (Number): product id
    - `product_price` (Object): product price
      - `amount` (String): amount
      - `currency_code` (String): currency code
    - `product_name` (String): product name
    - `product_count` (Number): number of products
  - `logistics_info_list` (Object[]): order logistics information list
    - `logistics_no` (String): logistics tracking number
    - `logistics_service` (String): logistics service
  - `store_info` (Object): store Information
    - `store_id` (Number): store id
    - `store_name` (String): store name
    - `store_url` (String): store url

**Errores:** `isv.insufficient-permission`: Insufficient permissions，please check the parameters; `isp.service-unavailable`: Service timed out, please try again; `isv.invalid-authorization`: Accessing data not belonging to you，please check the parameters; `InternalError`: System error,Need to contact technical support