AUTHOR = "Mindwrapper"
SITENAME = "Mindwrapper"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Amsterdam"

DEFAULT_LANG = "en"

THEME = "themes/Flex"
PLUGINS = ["sitemap", "neighbors"]  # Add plugins if needed

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)
# sitemap

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
}

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
