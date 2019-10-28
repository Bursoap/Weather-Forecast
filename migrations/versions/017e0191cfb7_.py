"""empty message

Revision ID: 017e0191cfb7
Revises: aafa879869d4
Create Date: 2019-10-28 12:27:37.802252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017e0191cfb7'
down_revision = 'aafa879869d4'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('city', 'lon', type_=sa.Float(9),
                    existing_type=sa.Numeric)
    op.alter_column('city', 'lat', type_=sa.Float(9),
                    existing_type=sa.Numeric)

    op.alter_column('forecast', 'temp', type_=sa.Float(4),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'temp_min', type_=sa.Float(4),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'temp_max', type_=sa.Float(4),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'pressure', type_=sa.Float(6),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'sea_level', type_=sa.Float(6),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'grnd_level', type_=sa.Float(6),
                    existing_type=sa.Numeric)
    op.alter_column('forecast', 'wind_speed', type_=sa.Float(5),
                    existing_type=sa.Numeric)


def downgrade():
    op.alter_column('city', 'lon',
                    type_=sa.Numeric(precision=9, scale=6),
                    existing_type=sa.Float)
    op.alter_column('city', 'lat',
                    type_=sa.Numeric(precision=9, scale=6),
                    existing_type=sa.Float)

    op.alter_column('forecast', 'temp',
                    type_=sa.Numeric(precision=4, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'temp_min',
                    type_=sa.Numeric(precision=4, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'temp_max',
                    type_=sa.Numeric(precision=4, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'pressure',
                    type_=sa.Numeric(precision=6, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'sea_level',
                    type_=sa.Numeric(precision=6, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'grnd_level',
                    type_=sa.Numeric(precision=6, scale=2),
                    existing_type=sa.Float)
    op.alter_column('forecast', 'wind_speed',
                    type_=sa.Numeric(precision=5, scale=2),
                    existing_type=sa.Float)
