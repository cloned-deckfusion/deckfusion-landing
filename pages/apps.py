# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PAGES CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class PagesConfig(AppConfig):
    """Pages Config"""

    # Define name
    name = "pages"

    # Define default auto field
    default_auto_field = "django.db.models.BigAutoField"
