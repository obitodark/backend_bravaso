"""add model sucategories and relation widht categories

Revision ID: a5b48e453e52
Revises: bb3c566025b3
Create Date: 2022-09-14 17:30:28.507537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5b48e453e52'
down_revision = 'bb3c566025b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subcategories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('id_category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_category'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subcategories')
    # ### end Alembic commands ###
