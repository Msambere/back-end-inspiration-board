"""empty message

Revision ID: f20db106ce1f
Revises: dcd7580388a5
Create Date: 2024-12-30 15:28:31.072173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f20db106ce1f'
down_revision = 'dcd7580388a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('board_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.alter_column('board_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
