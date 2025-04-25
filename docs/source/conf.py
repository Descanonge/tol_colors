# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Tol-colors"
copyright = "2025, Clément Haëck, Paul Tol"
author = "Clément Haëck, Paul Tol"
release = "2.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "Tol-colors"
html_theme_options = dict(
    collapse_navigation=False,
    use_download_button=True,
    use_fullscreen_button=False,
    # TOC
    show_toc_level=2,
    # Link to source in repo
    repository_url="https://github.com/Descanonge/tol_colors",
    use_source_button=True,
    repository_branch="master",
    path_to_docs="docs",
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
    # Footer
    article_footer_items=[],
    content_footer_items=[],
    # footer_start=["footer-left"],
    footer_end=["footer-right"],
)
html_last_updated_fmt = "%Y-%m-%d"

html_sidebars = {"**": ["navbar-logo.html", "sbt-sidebar-nav.html", "icon-links.html"]}
