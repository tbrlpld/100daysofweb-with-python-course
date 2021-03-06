"""Remove exmaple model

Revision ID: cea43510db50
Revises: 33a11ee0d534
Create Date: 2019-11-24 17:18:16.737040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cea43510db50'
down_revision = '33a11ee0d534'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_models')
    )
    op.create_index('my_index', 'models', ['name'], unique=1)
    # ### end Alembic commands ###
