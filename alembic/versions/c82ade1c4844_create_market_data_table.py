"""Create Market Data Table

Revision ID: c82ade1c4844
Revises: 9d6aac89bad4
Create Date: 2024-08-19 10:12:40.656833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c82ade1c4844'
down_revision: Union[str, None] = '9d6aac89bad4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'market',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('symbol_id', sa.Integer(), nullable=False),
        sa.Column('price_change', sa.DECIMAL(30, 10)),
        sa.Column('price_change_percent', sa.DECIMAL(30, 10)),
        sa.Column('weighted_avg_price', sa.DECIMAL(30, 10)),
        sa.Column('prev_close_price', sa.DECIMAL(30, 10)),
        sa.Column('last_price', sa.DECIMAL(30, 10)),
        sa.Column('last_qty', sa.DECIMAL(30, 10)),
        sa.Column('bid_price', sa.DECIMAL(30, 10)),
        sa.Column('bid_qty', sa.DECIMAL(30, 10)),
        sa.Column('ask_price', sa.DECIMAL(30, 10)),
        sa.Column('ask_qty', sa.DECIMAL(30, 10)),
        sa.Column('open_price', sa.DECIMAL(30, 10)),
        sa.Column('high_price', sa.DECIMAL(30, 10)),
        sa.Column('low_price', sa.DECIMAL(30, 10)),
        sa.Column('volume', sa.DECIMAL(30, 10)),
        sa.Column('quote_volume', sa.DECIMAL(30, 10)),
        sa.Column('open_time', sa.BigInteger()),
        sa.Column('close_time', sa.BigInteger()),
        sa.Column('first_id', sa.BigInteger()),
        sa.Column('last_id', sa.BigInteger()),
        sa.Column('count', sa.BigInteger()),
        sa.Column('created_at', sa.DateTime()),
    )


def downgrade() -> None:
    op.drop_table('market')