from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard(disabled_category: str = None):
    buttons = []
    for cat in ["Документы", "Учебный процесс", "Служба заботы", "Другое"]:
        if cat == disabled_category:
            buttons.append([InlineKeyboardButton(text=f"• {cat}", callback_data="ignore")])
        else:
            buttons.append([InlineKeyboardButton(text=cat, callback_data=cat)])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_submenu_keyboard(category: str):
    buttons = []

    if category == "Другое":
        buttons.extend([
            InlineKeyboardButton(text="Проблемы с техникой", callback_data="Проблемы с техникой"),
            InlineKeyboardButton(text="Обратная связь", callback_data="Обратная связь"),
            InlineKeyboardButton(text="Срочная помощь", callback_data="Срочная помощь")
        ])

    buttons.append(InlineKeyboardButton(text="Назад", callback_data="back_to_main"))
    return InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
