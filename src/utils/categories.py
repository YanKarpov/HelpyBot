from dataclasses import dataclass

@dataclass(frozen=True)
class CategoryInfo:
    image: str
    text: str

CATEGORIES = {
    "Документы": CategoryInfo(
        image="assets/images/documents.jpg",
        text=(
            "Если тебя интересует один из перечисленных вопросов — тебе необходимо обратиться в Учебный отдел📚\n"
            "Он находится на 4-ом этаже рядом с аудиторией 4.2."
        )
    ),
    "Учебный процесс": CategoryInfo(
        image="assets/images/study.jpg",
        text=(
            "Если тебя интересует один из перечисленных вопросов — тебе необходимо обратиться на свою кафедру⚡️\n"
            "Кафедры расположены на 4-ом этаже рядом со столовой.\n\n"
            "💡Подсказка💡\n"
            "Свою кафедру вы можете узнать по первым буквам в названии группы:\n"
            "— Д — Кафедра дизайна\n"
            "— ИБ — Кафедра информационной безопасности\n"
            "— ИТ — Кафедра информационных технологий\n"
            "— МК — Кафедра маркетинга\n"
            "— РИ — Кафедра разработки игр"
        )
    ),
    "Служба заботы": CategoryInfo(
        image="assets/images/support.jpg",
        text=(
            "Если тебя интересует один из перечисленных вопросов — тебе необходимо обратиться в кабинет Службы заботы💜\n"
            "Он находится на третьем этаже рядом с коворкингом."
        )
    ),
    "Другое": CategoryInfo(
        image="assets/images/other.jpg",
        text="Если ни один из пунктов тебе не подошел, можешь ознакомиться с нашим дополнительным меню:"
    )
}

SUBCATEGORIES = {
    "Обратная связь": CategoryInfo(
        image="assets/images/feedback.jpg",
        text=(
            "Здесь ты можешь оставить обратную связь касаемо работы или задать интересующие тебя вопросы:"
        )
    ),
    "Проблемы с техникой": CategoryInfo(
        image="assets/images/tech_issues.jpg",
        text=(
            "Если ты столкнулся с какой-то технической проблемой — подробно опиши ее в формате:\n"
            "1. Название и номер устройства\n"
            "2. Описание проблемы"
        )
    ),
    "Срочная помощь": CategoryInfo(
        image="assets/images/other_sub.jpg",
        text=(
            "Данная кнопка предназначена для того чтобы ты мог анонимно рассказать о чрезвычайных ситуациях, с которыми ты столкнулся."
        )
    ),
}


START_INFO = CategoryInfo(
    image="assets/images/welcome.jpg",
    text=(
        "Привет, {full_name}!\n"
        "Мы знаем, что у тебя могло возникнуть множество вопросов, и с радостью готовы помочь тебе их решить 💜\n\n"
        "Выбери категорию, к которой относится твой вопрос:"
    )
)

FEEDBACK_NOTIFICATION_TEMPLATE = (
    "Новое обращение от {sender_display_name}:\n"
    "Категория: {category}\n\n"
    "{message_text}"
)

ACKNOWLEDGMENT_CAPTION = "Спасибо! Твое сообщение отправлено в службу поддержки."
ACKNOWLEDGMENT_IMAGE_PATH = "assets/images/support_received.jpg"

CATEGORIES_LIST = list(CATEGORIES.keys())
