from distutils.core import setup

setup(
    name = "mezzanine_superfish",
    version = "0.1.0",
    author = "audreyr",
    author_email = "audreyr@cartwheelweb.com",
    description = "Superfish dropdown menus for Mezzanine",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/cartwheelweb/mezzanine_superfish",
    packages = [
        "mezzanine_superfish",
        "mezzanine_superfish.templatetags",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
