from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charity_project_crud
from app.models import CharityProject, Donation, User


async def check_name_duplicate(
    project_name: str, session: AsyncSession
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Проект с таким названием уже существует",
        )


# async def check_charity_project_exists(
#     project_id: int, session: AsyncSession
# ) -> CharityProject:
#     project = await charity_project_crud.get(project_id, session)
#     if project is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Проект не найден!"
#         )
#     return project


# async def check_reservation_intersections(**kwargs) -> None:
#     reservations = await reservation_crud.get_reservations_at_the_same_time(
#         **kwargs
#     )
#     print(bool(reservations))
#     if reservations:
#         raise HTTPException(status_code=422, detail=str(reservations))
#     return None


async def check_project_before_edit(
    project_id: int, session: AsyncSession, user: User
) -> CharityProject:
    project = await charity_project_crud.get(
        obj_id=project_id, session=session
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Проект не найден!"
        )
    if project.fully_invested:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Невозможно редактировать закрытый проект!",
        )
    return project
