"""empty message

Revision ID: c47235fff6f4
Revises: 954967dc4cde
Create Date: 2019-09-17 18:54:20.131023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c47235fff6f4'
down_revision = '954967dc4cde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('regtb', 'userid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('regtb', sa.Column('userid', sa.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###
