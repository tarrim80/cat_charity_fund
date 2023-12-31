from datetime import datetime
from typing import Optional

from fastapi import HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import ErrorMsg
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
    project_name: str, session: AsyncSession
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorMsg.PROJECT_ALREADY_EXISTS,
        )


async def check_charity_project_fully_invested(
    charity_project: CharityProject,
    session: AsyncSession,
    obj_in_data: dict,
) -> CharityProject:
    if obj_in_data["full_amount"] == charity_project.invested_amount:
        charity_project.fully_invested = True
        charity_project.close_date = datetime.now()
    return charity_project


async def check_project_before_edit(
    project_id: int,
    session: AsyncSession,
    request: Request,
    obj_in_data: Optional[dict] = None,
) -> CharityProject:
    project = await charity_project_crud.get(
        obj_id=project_id, session=session
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ErrorMsg.PROJECT_NOT_FOUND,
        )
    if request.method == "PATCH":
        if project.fully_invested:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMsg.PROJECT_CLOSE,
            )
        if obj_in_data["full_amount"] and (
            project.invested_amount > obj_in_data["full_amount"]
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorMsg.AMOUNT_LESS_THAN_INVESTED,
            )
        if not any(obj_in_data.values()):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=ErrorMsg.EDITING_NOT_PROVIDED,
            )
    if request.method == "DELETE" and (
        project.invested_amount != 0 or project.fully_invested
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorMsg.INVESTED_NOT_EMPTY,
        )
    return project
