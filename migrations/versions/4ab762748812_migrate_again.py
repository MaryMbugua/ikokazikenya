"""migrate again

Revision ID: 4ab762748812
Revises: 4fd2ad76e41b
Create Date: 2018-02-16 02:21:23.841200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ab762748812'
down_revision = '4fd2ad76e41b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('adtitle', sa.String(length=255), nullable=True),
    sa.Column('adcontent', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('dateposted', sa.String(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobads')
    # ### end Alembic commands ###