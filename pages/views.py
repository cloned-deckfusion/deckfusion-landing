# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.conf import settings
from django.views.generic import TemplateView


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ HOME VIEW
# └─────────────────────────────────────────────────────────────────────────────────────


class HomeView(TemplateView):
    """Home View"""

    # Define template name
    template_name = "pages/index.html"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET CONTEXT DATA
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_context_data(self, **kwargs):
        """Get Context Data Method"""

        # Get context data
        context = super().get_context_data(**kwargs)

        # Add backend base URL
        context["BACKEND_BASE_URL"] = settings.BACKEND_BASE_URL

        # Return context
        return context


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CONTACT VIEW
# └─────────────────────────────────────────────────────────────────────────────────────


class ContactView(TemplateView):
    """Contact View"""

    # Define template name
    template_name = "pages/contact.html"

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ GET CONTEXT DATA
    # └─────────────────────────────────────────────────────────────────────────────────

    def get_context_data(self, **kwargs):
        """Get Context Data Method"""

        # Get context data
        context = super().get_context_data(**kwargs)

        # Add backend base URL
        context["BACKEND_BASE_URL"] = settings.BACKEND_BASE_URL

        # Return context
        return context
