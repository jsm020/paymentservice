from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


# ds_praktikum = Product(
#     title="Data Science va Sun'iy intellekt",
#     description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
#     currency="UZS",
#     prices=[
#         LabeledPrice(
#             label='Praktikum',
#             amount=150000000, #150.00$
#         ),
#         LabeledPrice(
#             label='Chegirma',
#             amount=-10000000, #-10.00$
#         ),
#     ],
#     start_parameter="create_invoice_ds_praktikum",
#     photo_url='https://i.imgur.com/vRN7PBT.jpg',
#     photo_width=1280,
#     photo_height=564,
#     # photo_size=600,
#     need_email=True,
#     need_name=True,
#     need_phone_number=True,
# )

python_book = Product(
    title="Mackbook Pro 14",
    description="Kompyuterga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Mackbook',
            amount=900000000,#5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=3500000,#1.00$
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://img.mvideo.ru/Big/400029358bb.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100000),
        LabeledPrice(
            '3 ish kunida yetkazish', 100000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 150000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100000)
                                       ])