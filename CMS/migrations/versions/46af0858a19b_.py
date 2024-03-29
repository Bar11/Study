"""empty message

Revision ID: 46af0858a19b
Revises: 
Create Date: 2019-11-26 18:21:41.519516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46af0858a19b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfo',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('salt', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userinfo')
    # ### end Alembic commands ###
