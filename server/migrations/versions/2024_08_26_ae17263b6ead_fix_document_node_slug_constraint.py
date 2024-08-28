"""Fix document node slug constraint

Revision ID: ae17263b6ead
Revises: 438caa40032e
Create Date: 2024-08-26 19:54:23.294467

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ae17263b6ead"
down_revision: Union[str, None] = "438caa40032e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("uq_document_nodes_slug", "document_nodes", type_="unique")
    op.create_unique_constraint(
        op.f("uq_document_nodes_slug"),
        "document_nodes",
        ["slug", "document_translation_id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("uq_document_nodes_slug"), "document_nodes", type_="unique")
    op.create_unique_constraint("uq_document_nodes_slug", "document_nodes", ["slug"])
    # ### end Alembic commands ###