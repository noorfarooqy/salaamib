"""merge login_security_fields

Revision ID: 553448097257
Revises: 1b7d677b35e1, b869d58b89be
Create Date: 2025-03-16 07:50:58.579866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '553448097257'
down_revision: Union[str, None] = ('1b7d677b35e1', 'b869d58b89be')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
