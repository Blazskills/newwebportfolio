"""empty message

Revision ID: b96c59ee34a0
Revises: 4fab9029c2a6
Create Date: 2019-09-17 19:37:41.140576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b96c59ee34a0'
down_revision = '4fab9029c2a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('regtb', sa.Column('userid2', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('regtb', 'userid2')
    # ### end Alembic commands ###
