from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_project_fully_invested,
    check_name_duplicate,
    check_project_before_edit,
)
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)

router = APIRouter()


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Создает благотворительный проект.
    """

    await check_name_duplicate(charity_project.name, session)
    # new_project = await check_charity_project_fully_invested(
    #     charity_project=charity_project, session=session
    # )
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
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    request: Request,
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Удаляет проект. Нельзя удалить проект, в который уже были инвестированы
    средства, его можно только закрыть.
    """
    charity_project = await check_project_before_edit(
        project_id=project_id, session=session, request=request
    )
    charity_project = await charity_project_crud.remove(
        charity_project, session
    )
    return charity_project


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    *,
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
    request: Request,
):
    """Только для суперюзеров.

    Закрытый проект нельзя редактировать, также нельзя установить требуемую
    сумму меньше уже вложенной.
    """
    obj_in_data = obj_in.dict()
    await check_name_duplicate(obj_in.name, session)
    charity_project = await check_project_before_edit(
        project_id=project_id,
        obj_in_data=obj_in_data,
        session=session,
        request=request,
    )
    charity_project = await charity_project_crud.update(
        db_obj=charity_project, obj_in=obj_in, session=session
    )
    return charity_project
