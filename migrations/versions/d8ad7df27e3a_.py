"""empty message

Revision ID: d8ad7df27e3a
Revises: 5c9c73e35be2
Create Date: 2019-09-17 19:22:29.694594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8ad7df27e3a'
down_revision = '5c9c73e35be2'
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