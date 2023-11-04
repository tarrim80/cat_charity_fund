from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate
from app.core.db import get_async_session
from app.crud.charityproject import charity_project_crud
from app.schemas.charityproject import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)

router = APIRouter()


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Создает благотворительный проект.
    """

    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    return new_project


@router.get(
    "/",
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    """Получает список всех проектов."""
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def delete_charity_project(
    project_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров.

    Удаляет проект. Нельзя удалить проект, в который уже были инвестированы
    средства, его можно только закрыть.
    """
    pass


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Закрытый проект нельзя редактировать, также нельзя установить требуемую
    сумму меньше уже вложенной.
    """
    pass
