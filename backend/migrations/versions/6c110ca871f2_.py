"""empty message

Revision ID: 6c110ca871f2
Revises: d9bce6030b72
Create Date: 2021-03-14 10:34:59.285942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c110ca871f2'
down_revision = 'd9bce6030b72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('urls', 'slug',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('urls', 'slug',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
