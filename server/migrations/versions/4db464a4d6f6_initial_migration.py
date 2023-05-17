"""Initial migration.

Revision ID: 4db464a4d6f6
Revises: 6018d594fa3b
Create Date: 2023-05-16 16:12:15.504277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4db464a4d6f6'
down_revision = '6018d594fa3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_column('unit_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unit_price', sa.NUMERIC(), nullable=False))

    # ### end Alembic commands ###
