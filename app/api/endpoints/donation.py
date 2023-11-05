from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_name_duplicate
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import DonationCreate, DonationDB

router = APIRouter()


@router.post(
    "/",
    response_model=DonationDB,
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Сделать пожертвование."""

    # await check_name_duplicate(donation.name, session)
    new_project = await donation_crud.create(donation, session)
    return new_project


@router.get(
    "/",
    response_model=list[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров.

    Получает список всех пожертвований.
    """
    all_projects = await donation_crud.get_multi(session)
    return all_projects


@router.get(
    "/my",
    response_model=list[DonationDB],
    response_model_exclude={"user_id"},
    response_model_exclude_defaults=True,
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Получить список моих пожертвований."""
    my_reservations = await donation_crud.get_by_user(
        session=session, user=user
    )
    return my_reservations
