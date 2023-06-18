"""empty message

Revision ID: e75c72afb20b
Revises: c6970f473e04
Create Date: 2023-06-18 11:26:51.835903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e75c72afb20b'
down_revision = 'c6970f473e04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('e_med_card')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('e_med_card',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('disease', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('treatment', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('patient', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('doctor', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['doctor'], ['users.id'], name='fk_e_med_card_users_id_doctor', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['patient'], ['users.id'], name='fk_e_med_card_users_id_patient', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='e_med_card_pkey')
    )
    # ### end Alembic commands ###