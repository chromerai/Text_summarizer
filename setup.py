import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()



__version__ = "0.0.1"
REPO_NAME = "Text_summarizer"
AUTHOR_USER_NAME = 'chromerai'
SRC_REPO = "Project_text_summarizer"
AUTHOR_EMAIL = "kaustubhmishra983@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A python package for text_summarizer NLP app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where= "src")
)