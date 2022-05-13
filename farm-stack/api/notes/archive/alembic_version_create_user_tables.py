"""Create user tables

Revision ID: 956d84f7a801
Revises: 
Create Date: 2022-01-23 03:43:57.799954

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision = 'Template'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users", 
        sa.Column("id", UUID(as_uuid=True), nullable=False, primary_key=True),
        sa.Column("user_name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("api_key", UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
        
        # id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
        # user_name = Column(String, nullable=False)
        # email = Column(String, nullable=False, unique=True)
        # password = Column(String, nullable=False)
        # api_key = Column(UUID(as_uuid=True), nullable=False)
        # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
