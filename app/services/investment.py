from datetime import datetime
from typing import Union

from sqlalchemy import not_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation

Entity = Union[Donation, CharityProject]


async def investment(session: AsyncSession, entity: Entity) -> Entity:
    """Старт процесса инвестирования."""
    entity2 = CharityProject if isinstance(entity, Donation) else Donation
    return await distributing_investment(
        session=session, entity1=entity, entity2=entity2
    )


async def distributing_investment(
    session: AsyncSession,
    entity1: Entity,
    entity2: Entity,
) -> Entity:
    """Распределение инвестиций."""

    if entity1.fully_invested:
        return entity1

    stmt = await session.execute(
        select(entity2).where(not_(entity2.fully_invested))
    )
    open_entity = stmt.scalars().first()

    if open_entity is None:
        return entity1

    entities = [entity1, open_entity]
    min_entity = min(entities, key=lambda x: x.missing_amount)
    max_entity = entities[0] if min_entity == entities[1] else entities[1]

    await increase_invested_amount(
        entities=entities, amount=min_entity.missing_amount
    )
    await close_investment(entity=min_entity)

    if all(
        entity.missing_amount == entities[0].missing_amount
        for entity in entities
    ):
        await close_investment(entity=max_entity)

    await update_db(entities=entities, session=session)
    return await distributing_investment(
        session=session, entity1=entity1, entity2=entity2
    )


async def increase_invested_amount(entities: list[Entity], amount) -> None:
    """Увеличение `invested_amount` в проекте и в пожертвовании."""
    for entity in entities:
        entity.invested_amount += amount


async def close_investment(entity) -> None:
    """Закрытие инвестиций в проект или закрытие пожертвования."""
    if entity.full_amount != entity.invested_amount:
        return
    entity.fully_invested = True
    entity.close_date = datetime.now()


async def update_db(entities: list[Entity], session: AsyncSession) -> None:
    """Обновление базы данных."""
    for entity in entities:
        session.add(entity)
    await session.commit()
    await session.refresh(entities[0])
