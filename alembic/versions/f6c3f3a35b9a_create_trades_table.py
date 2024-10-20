"""Create Trades Table

Revision ID: f6c3f3a35b9a
Revises: c82ade1c4844
Create Date: 2024-09-01 10:02:35.868704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6c3f3a35b9a'
down_revision: Union[str, None] = 'c82ade1c4844'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.create_table(
        'trades',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('bot_id', sa.Integer(), nullable=False),
        sa.Column('symbol_id', sa.Integer(), nullable=False),
        sa.Column('market_id_buyin', sa.Integer(), nullable=False),
        sa.Column('market_id_sellout',  sa.Integer(), nullable=True),
        sa.Column('value_buyin', sa.DECIMAL(30, 10)),
        sa.Column('value_sellout', sa.DECIMAL(30, 10)),
        sa.Column('datetime_buyin', sa.DateTime()),
        sa.Column('datetime_sellout', sa.DateTime()),
        sa.Column('percentage_difference', sa.DECIMAL(30, 10)),
        sa.Column('total_percentage_change', sa.DECIMAL(30, 10)),
    )


def downgrade() -> None:
    op.drop_table('trades')
