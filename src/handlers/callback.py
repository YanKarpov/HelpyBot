from aiogram.types import CallbackQuery
from src.keyboard import get_main_keyboard, get_submenu_keyboard
from src.state import admin_replying
from src.handlers.utils import save_feedback_state, send_or_edit_media

from src.logger import setup_logger

logger = setup_logger(__name__)

categories = ["Документы", "Учебный процесс", "Служба заботы", "Другое"]

category_pictures = {
    "Документы": "images/documents.jpg",
    "Учебный процесс": "images/study.jpg",
    "Служба заботы": "images/support.jpg",
    "Другое": "images/other.webp",
}

category_texts = {
    "Документы": "Тебе поможет учебный отдел, он находится на 4 этаже рядом с кабинетом 4.2",
    "Учебный процесс": "Ты можешь обратиться на свою кафедру. Она находится на 4 этаже напротив столовой",
    "Служба заботы": "Обратись в кабинет службы заботы на 3 этаже рядом с кабинетом 3.8",
    "Другое": "Разные полезные сведения.",
}


async def callback_handler(callback: CallbackQuery):
    data = callback.data
    user_id = callback.from_user.id
    logger.info(f"Callback received from user {user_id} with data: {data}")

    async def save_menu_id(msg):
        await save_feedback_state(user_id, menu_message_id=msg.message_id)
        logger.info(f"Menu message id={msg.message_id} saved for user {user_id}")

    if data.startswith("reply_to_user:"):
        try:
            admin_replying[callback.from_user.id] = int(data.split(":", 1)[1])
            await callback.answer("Напиши сообщение для пользователя в этом чате")
            await callback.message.answer(f"Ответ пользователю ID {admin_replying[callback.from_user.id]}:")
            logger.info(f"Admin {callback.from_user.id} replying to user {admin_replying[callback.from_user.id]}")
        except ValueError:
            logger.error(f"Invalid user ID in reply_to_user: {data}")
            await callback.answer("Некорректный ID", show_alert=True)
        return

    if data == "back_to_main":
        msg = await send_or_edit_media(
            callback.message,
            "images/other.webp",
            f"Привет, {callback.from_user.full_name}!\nЯ знаю, что у тебя вопрос и я постараюсь его решить ❤️",
            get_main_keyboard()
        )
        await save_menu_id(msg)
        await callback.answer()
        return

    if data == "ignore":
        await callback.answer("Вы уже здесь 😉", show_alert=True)
        logger.info(f"User {user_id} pressed ignore")
        return

    if data in ["Проблемы с техникой", "Обратная связь"]:
        prompt_msg = await callback.message.answer(f"Опиши проблему по теме '{data}':")
        await save_feedback_state(user_id, type=data, prompt_message_id=prompt_msg.message_id)
        logger.info(f"Feedback prompt sent to user {user_id} for type {data}")
        await callback.answer()
        return

    if data == "Другое":
        msg = await send_or_edit_media(
            callback.message,
            category_pictures["Другое"],
            category_texts["Другое"],
            get_submenu_keyboard("Другое")
        )
        await save_menu_id(msg)
        await callback.answer()
        return

    if data in categories:
        msg = await send_or_edit_media(
            callback.message,
            category_pictures[data],
            category_texts[data],
            get_main_keyboard(disabled_category=data)
        )
        await save_menu_id(msg)
        await callback.answer()
        return

    logger.warning(f"Unknown callback data received: {data}")
    await callback.answer("Неизвестная команда", show_alert=True)
