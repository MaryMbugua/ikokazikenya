"""update employees table  migration

Revision ID: 4fd2ad76e41b
Revises: 92e191f3e728
Create Date: 2018-02-12 16:06:12.909338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd2ad76e41b'
down_revision = '92e191f3e728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('age', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('contact', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('experience', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('gender', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('location', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('profilepic_path', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('skill', sa.String(length=255), nullable=True))
    op.add_column('employees', sa.Column('status', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'status')
    op.drop_column('employees', 'skill')
    op.drop_column('employees', 'profilepic_path')
    op.drop_column('employees', 'location')
    op.drop_column('employees', 'gender')
    op.drop_column('employees', 'experience')
    op.drop_column('employees', 'contact')
    op.drop_column('employees', 'category')
    op.drop_column('employees', 'age')
    # ### end Alembic commands ###