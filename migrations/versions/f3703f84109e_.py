"""empty message

Revision ID: f3703f84109e
Revises: adad5ecaab00
Create Date: 2020-12-26 16:04:11.157971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3703f84109e'
down_revision = 'adad5ecaab00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('missing_check_penalty', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedules', 'missing_check_penalty')
    # ### end Alembic commands ###
