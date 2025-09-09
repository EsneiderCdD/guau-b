"""limpiar match_usuarios: drop columnas viejas y add 4D

Revision ID: 5a323573140c
Revises: 77cb9673be96
Create Date: 2025-09-08 20:59:57.082794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a323573140c'
down_revision = '77cb9673be96'
branch_labels = None
depends_on = None


def upgrade():
    # 1) Borrar columnas antiguas
    with op.batch_alter_table('match_usuarios', schema=None) as batch_op:
        batch_op.drop_column('tiempo_disponible')
        batch_op.drop_column('experiencia')
        batch_op.drop_column('apego_emocional')

    # 2) Agregar columnas nuevas
    with op.batch_alter_table('match_usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('energia', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('apego_vinculo', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('regulacion_emocional', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('exploracion_libertad', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # 3) Limpiar datos obsoletos
    op.execute("DELETE FROM match_usuarios;")


def downgrade():
    # Revertir cambios: borrar nuevas columnas y restaurar las viejas
    with op.batch_alter_table('match_usuarios', schema=None) as batch_op:
        batch_op.drop_column('energia')
        batch_op.drop_column('apego_vinculo')
        batch_op.drop_column('regulacion_emocional')
        batch_op.drop_column('exploracion_libertad')
        batch_op.drop_column('updated_at')

        batch_op.add_column(sa.Column('tiempo_disponible', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('experiencia', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('apego_emocional', sa.Integer(), nullable=True))
