from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import DonationCreate, DonationDB, DonationResponse
from app.services.investment import investment

router = APIRouter()


@router.post(
    "/",
    response_model=DonationResponse,
    response_model_exclude_none=True,
    response_model_exclude_defaults=True,
    dependencies=[Depends(current_user)],
)
async def create_donation(
    *,
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Сделать пожертвование."""

    new_donation = await donation_crud.create(
        obj_in=donation, session=session, user=user
    )
    return await investment(session=session, entity=new_donation)


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

    Возвращает список всех пожертвований.
    """
    return await donation_crud.get_multi(session)


@router.get(
    "/my",
    response_model=list[DonationResponse],
    response_model_exclude={
        "user_id",
    },
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    return await donation_crud.get_by_user(session=session, user=user)
