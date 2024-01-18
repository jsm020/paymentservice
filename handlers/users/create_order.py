from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.products import python_book,  FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
from keyboards.inline.product_keys import build_keyboard


@dp.message_handler(Command("kitob"))
async def show_invoices(message: types.Message):
    caption = "<b>Mackbook Pro 19</b> kompyuter.\n\n"
    caption += "🖥 Ekran O'lchami: 15'6\n\n"
    caption += "⚙️ Protsessor: Intel Corei9"
    caption += "⏳ Operativka : 16GB.\n\n"
    caption += "SSD : 512GB\n\n"
    caption += "Narxi: <b>9000000so`m</b>"
    await message.answer_photo(photo="https://img.mvideo.ru/Big/400029358bb.jpg",
                         caption=caption, reply_markup=build_keyboard("book"))

# @dp.message_handler(Command("praktikum"))
# async def show_invoices(message: types.Message):
#     caption = "<b>Data Science va Sun'iy Intellekt</b> praktikum.\n\n"
#     caption += "6 oyda eng zamonaviy kasb egasi bo'ling.\n\n"
#     caption += "Kurs tarkibi:\n"
#     caption += "✅ Python Dasturlash Asoslar (4 hafta)\n"
#     caption += "✅ Data Sciencega kirish va DS metodologiyasi (2 hafta)\n"
#     caption += "✅ Maʻlumotlar tahlili (Data Analysis) (4 hafta)\n"
#     caption += "✅ Maʻlumotlarga ishlov berish (4 hafta)\n"
#     caption += "✅ Vizualizasiya (2 hafta)\n"
#     caption += "✅ Machine Learning (6 hafta)\n"
#     caption += "✅ Deep Learning (4 hafta)\n"
#     caption += "✅ Natural Language Processing (4 hafta)\n\n"
#     caption += "Narxi: <b>1.5mln so'm</b>"

#     await message.answer_photo(photo="https://i.imgur.com/vRN7PBT.jpg",
#                          caption=caption, reply_markup=build_keyboard("praktikum"))

@dp.message_handler(Command("mahsulotlar"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    # await bot.send_invoice(chat_id=message.from_user.id,
    #                        **ds_praktikum.generate_invoice(),
    #                        payload="123457")

@dp.callback_query_handler(text="product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:kitob")
    await call.answer()


# @dp.callback_query_handler(text="product:praktikum")
# async def praktikum_invoice(call: CallbackQuery):
#     await bot.send_invoice(chat_id=call.from_user.id,
#                            **ds_praktikum.generate_invoice(),
#                            payload="payload:praktikum")
#     await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")