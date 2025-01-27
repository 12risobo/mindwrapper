AUTHOR = "Mindwrapper"
SITENAME = "Mindwrapper"
SITEURL = "https://clever-fairy-a2cd86.netlify.app/"

SITETITLE = "MindWrapper"  # Customize these
SITESUBTITLE = "A Blog About Python & Web Dev"

PATH = "content"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

THEME = "themes/Flex"
PLUGINS = ["sitemap", "neighbors"]  # Add plugins if needed

STATIC_PATHS = ["images", "static"]
THEME_STATIC_DIR = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("GitHub", "https://github.com/12risobo/mindwrapper"),)
# sitemap

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
}

# Hide default "Built with Pelican..." footer
HIDE_SITENAME = True

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
