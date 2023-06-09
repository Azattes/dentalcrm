"""empty message

Revision ID: 868741462087
Revises: 2d17b10f78cb
Create Date: 2023-06-04 12:50:31.999457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '868741462087'
down_revision = '2d17b10f78cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('allergy', sa.Column('emedcard', sa.Integer(), nullable=True))
    op.drop_constraint('fk_allergy_users_id_user', 'allergy', type_='foreignkey')
    op.create_foreign_key('fk_allergy_e_med_card_id_emedcard', 'allergy', 'e_med_card', ['emedcard'], ['id'])
    op.drop_column('allergy', 'user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('allergy', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('fk_allergy_e_med_card_id_emedcard', 'allergy', type_='foreignkey')
    op.create_foreign_key('fk_allergy_users_id_user', 'allergy', 'users', ['user'], ['id'])
    op.drop_column('allergy', 'emedcard')
    # ### end Alembic commands ###
