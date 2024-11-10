# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.views.generic import TemplateView


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ HOME VIEW
# └─────────────────────────────────────────────────────────────────────────────────────


class HomeView(TemplateView):
    """Home View"""

    # Define template name
    template_name = "pages/index.html"
