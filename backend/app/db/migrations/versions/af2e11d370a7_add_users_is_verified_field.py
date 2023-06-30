"""add users.is_verified field

Revision ID: af2e11d370a7
Revises: fdf8821871d7
Create Date: 2023-06-30 21:51:03.431784

"""
from alembic import op
import sqlalchemy as sa


revision = "af2e11d370a7"
down_revision = "fdf8821871d7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "is_verified",
            sa.Boolean(),
            nullable=False,
            default=False,
            server_default="0",
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "is_verified")
