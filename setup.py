import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


_version_ = "0.0.0"

REPO_NAME = "End-to-end-Machine-Learning-Projects-with-ML-flow"
AUTHOR_USER_NAME = "KIRTI-245"
SRC_REPO = "https://github.com/KIRTI-245/End-to-end-Machine-Learning-Projects-with-ML-flow.git"
AUTHOR_EMAIL = "kirti1147@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End-to-end Machine Learning Projects with MLflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KIRTI-245/End-to-end-Machine-Learning-Projects-with-ML-flow.git",
    project_urls={
        "Bug Tracker": "https://github.com/KIRTI-245/End-to-end-Machine-Learning-Projects-with-ML-flow/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)