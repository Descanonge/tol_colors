# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

from docutils.nodes import Element
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.osutil import copyfile
from sphinx.writers.html import HTMLTranslator

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Tol-colors"
copyright = "2025, Clément Haëck, Paul Tol"
author = "Clément Haëck, Paul Tol"
release = "2.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.napoleon", "sphinx.ext.autodoc", "sphinx.ext.intersphinx"]

templates_path = ["_templates"]
exclude_patterns = []

# Intersphinx
intersphinx_mapping = {"matplotlib": ("https://matplotlib.org/", None)}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "Tol-colors"
html_logo = "_static/icon.svg"
html_favicon = "_static/favicon.ico"
html_scaled_image_link = False
html_theme_options = dict(
    # Social icons
    icon_links=[
        dict(
            name="Repository",
            url="https://github.com/Descanonge/tol_colors",
            icon="fa-brands fa-github",
        ),
        dict(
            name="PyPI",
            url="https://pypi.org/tol-colors",
            icon="fa-brands fa-python",
        ),
    ],
    logo=dict(text="Tol-colors"),
    # TOC
    secondary_sidebar_items=["page-toc"],
    show_toc_level=2,
    collapse_navigation=False,
    # Navigation bar
    navbar_start=["navbar-logo", "navbar-icon-links"],
    navbar_center=["navbar-nav"],
    navbar_end=["search-button"],
    # Footer
    show_prev_next=False,
    article_footer_items=[],
    content_footer_items=[],
    footer_start=["copyright", "last-updated"],
    footer_end=["sphinx-version", "theme-version"],
)
html_last_updated_fmt = "%Y-%m-%d"

html_sidebars = {"**": []}

## Open links in new tab


class CmapImage(directives.images.Image):
    option_spec = directives.images.Image.option_spec

    @property
    def img_source(self) -> str:
        return f"img/cmap_{self.cmap_name}.svg"

    @property
    def viscm_source(self) -> str:
        return f"_images/cmap_viscm_{self.cmap_name}.svg"

    def run(self):
        env = self.state.document.settings.env
        cmap_name = self.arguments[0]

        viscm_src = f"img/cmap_viscm_{cmap_name}.svg"
        viscm_out = f"_images/cmap_viscm_{cmap_name}.svg"
        viscm_out_full = os.path.join(env.app.builder.outdir, viscm_out)
        os.makedirs(os.path.dirname(viscm_out_full), exist_ok=True)
        copyfile(os.path.join(env.app.builder.srcdir, viscm_src), viscm_out_full)

        self.arguments[0] = f"/img/cmap_{cmap_name}.svg"
        self.options["target"] = viscm_out
        self.options["class"] = ["img-padding", "newtab"]

        node = super().run()
        return node


class PatchedHTMLTranslator(HTMLTranslator):
    def visit_reference(self, node):
        if "newtab" in node.get("classes") or any(
            isinstance(c, Element) and "newtab" in c.get("classes")
            for c in node.children
        ):
            node["target"] = "_blank"

        super().visit_reference(node)


def setup(app: Sphinx):
    app.add_directive("cmap", CmapImage)
    app.set_translator("html", PatchedHTMLTranslator)
