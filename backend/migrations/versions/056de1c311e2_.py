"""empty message

Revision ID: 056de1c311e2
Revises: 54cd90c1cd83
Create Date: 2021-09-02 19:19:52.079903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056de1c311e2'
down_revision = '54cd90c1cd83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buyer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('product', sa.String(), nullable=True),
    sa.Column('product_type', sa.String(), nullable=True),
    sa.Column('product_description', sa.String(), nullable=True),
    sa.Column('product_image', sa.String(length=500), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['buyer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seller')
    op.drop_table('buyer')
    # ### end Alembic commands ###
