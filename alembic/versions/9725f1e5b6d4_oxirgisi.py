"""oxirgisi

Revision ID: 9725f1e5b6d4
Revises: eef134397799
Create Date: 2023-07-12 16:45:21.926528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9725f1e5b6d4'
down_revision = 'eef134397799'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=999), nullable=True),
    sa.Column('address', sa.String(length=999), nullable=True),
    sa.Column('map_long', sa.String(length=999), nullable=True),
    sa.Column('map_lat', sa.String(length=999), nullable=True),
    sa.Column('branch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('supplies', sa.Column('supplier_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplies', 'supplier_id')
    op.drop_table('suppliers')
    # ### end Alembic commands ###
