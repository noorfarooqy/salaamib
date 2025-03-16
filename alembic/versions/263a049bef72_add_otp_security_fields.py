"""add_otp_security_fields

Revision ID: 263a049bef72
Revises: b869d58b89be
Create Date: 2024-03-14 11:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '263a049bef72'
down_revision: Union[str, None] = 'b869d58b89be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add OTP security columns
    op.add_column('users', sa.Column('otp_attempts', sa.Integer(), nullable=False, server_default='0'))
    op.add_column('users', sa.Column('otp_locked_until', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    # Remove OTP security columns
    op.drop_column('users', 'otp_locked_until')
    op.drop_column('users', 'otp_attempts')
