"""empty message

Revision ID: 4fab9029c2a6
Revises: d8ad7df27e3a
Create Date: 2019-09-17 19:23:05.976526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fab9029c2a6'
down_revision = 'd8ad7df27e3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('regtb', 'userpix3')
    op.drop_column('regtb', 'userpix2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('regtb', sa.Column('userpix2', sa.VARCHAR(length=200), nullable=True))
    op.add_column('regtb', sa.Column('userpix3', sa.VARCHAR(length=200), nullable=True))
    # ### end Alembic commands ###