"""add pub date and archive status in vacancy

Revision ID: 86d01b07ff60
Revises: e6c280bd7e83
Create Date: 2022-07-02 16:44:28.860205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86d01b07ff60'
down_revision = 'e6c280bd7e83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancy', sa.Column('published_at', sa.DateTime(), nullable=True))
    op.add_column('vacancy', sa.Column('archive', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vacancy', 'archive')
    op.drop_column('vacancy', 'published_at')
    # ### end Alembic commands ###
