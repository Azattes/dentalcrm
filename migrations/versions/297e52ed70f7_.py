"""empty message

Revision ID: 297e52ed70f7
Revises: 08de75090048
Create Date: 2023-06-18 11:24:28.114017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '297e52ed70f7'
down_revision = '08de75090048'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_e_med_card_disease_id_disease', 'e_med_card', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('fk_e_med_card_disease_id_disease', 'e_med_card', 'disease', ['disease'], ['id'])
    # ### end Alembic commands ###
