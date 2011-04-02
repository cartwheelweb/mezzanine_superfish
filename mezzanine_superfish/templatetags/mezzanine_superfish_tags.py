import logging 

from collections import defaultdict

from django.core.urlresolvers import reverse
from django.template import TemplateSyntaxError, Variable

from mezzanine.pages.models import Page
from mezzanine import template
from mezzanine.template.loader import get_template

register = template.Library()

@register.render_tag
def superfish_submenu(context, token):
    """
    Return a list of child pages for the given parent, storing all
    pages in a dict in the context when first called using parents as keys
    for retrieval on subsequent recursive calls from the menu template.
    """
    # First arg could be the menu template file name, or the parent page.
    # Also allow for both to be used.
#    logging.debug('superfish_submenu')
    template_name = None
    parent_page = None
    parts = token.split_contents()[1:]
    for part in parts:
        part = Variable(part).resolve(context)
        if isinstance(part, unicode):
            template_name = part
        elif isinstance(part, Page):
            parent_page = part
    if template_name is None:
        try:
            template_name = "mezzanine_superfish/superfishtree.html"
#            template_name = context["menu_template_name"]
        except KeyError:
            error = "No template found for page_menu in: %s" % parts
            raise TemplateSyntaxError(error)
    context["menu_template_name"] = template_name
#    logging.debug("context['menu_template_name'] is " + context["menu_template_name"])
    if "menu_pages" not in context:
        pages = defaultdict(list)
        try:
            user = context["request"].user
            slug = context["request"].path
        except KeyError:
            user = None
            slug = ""
        for page in Page.objects.published(for_user=user).select_related(depth=2).order_by("_order"):
            page.set_menu_helpers(slug)
            pages[page.parent_id].append(page)
        context["menu_pages"] = pages
        context["on_home"] = slug == reverse("home")
    # ``branch_level`` must be stored against each page so that the
    # calculation of it is correctly applied. This looks weird but if we do
    # the ``branch_level`` as a separate arg to the template tag with the
    # addition performed on it, the addition occurs each time the template
    # tag is called rather than once per level.
    context["branch_level"] = 0
    if parent_page is not None:
        context["branch_level"] = parent_page.branch_level + 1
        parent_page = parent_page.id
    context["page_branch"] = context["menu_pages"].get(parent_page, [])
    for i, page in enumerate(context["page_branch"]):
        context["page_branch"][i].branch_level = context["branch_level"]
    t = get_template(template_name, context)
#    logging.debug(context["page_branch"])
    return t.render(context)
