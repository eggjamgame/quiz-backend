"""init

Revision ID: 7fdab0fa4a99
Revises: 
Create Date: 2022-04-12 05:25:50.916040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fdab0fa4a99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_category_id'), 'quiz_category', ['id'], unique=False)
    op.create_index(op.f('ix_quiz_category_title'), 'quiz_category', ['title'], unique=False)
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['quiz_category.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_quiz_id'), 'quiz', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_quiz_id'), table_name='quiz')
    op.drop_table('quiz')
    op.drop_index(op.f('ix_quiz_category_title'), table_name='quiz_category')
    op.drop_index(op.f('ix_quiz_category_id'), table_name='quiz_category')
    op.drop_table('quiz_category')
    # ### end Alembic commands ###
