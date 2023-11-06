MAX_NAME_LENGTH = 100
MIN_STRING_LENGTH = 1
MIN_AMOUNT = 1


class ErrorMsg:
    PROJECT_ALREADY_EXISTS = "Проект с таким именем уже существует!"
    PROJECT_NOT_FOUND = "Проект не найден!"
    PROJECT_CLOSE = "Закрытый проект нельзя редактировать!"
    AMOUNT_LESS_THAN_INVESTED = (
        "Запрещено устанавливать требуемую сумму меньше внесённой!"
    )
    EDITING_NOT_PROVIDED = (
        "Нельзя изменить значение полей, "
        "редактирование которых не предусмотрено"
    )
    INVESTED_NOT_EMPTY = (
        "В проект были внесены средства, не подлежит удалению!"
    )
    MUST_GREATER_THAN_ZERO = "Значение должно быть больше `0`."
