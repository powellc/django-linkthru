from setuptools import setup, find_packages

setup(
    name='django-linkthru',
    version=__import__('linkthru').__version__,
    license="GPLv3",

    install_requires = ['django-extensions',],

    description='A riff on adzone, but without the advert cruft. Just text/images linking to arbitrary urls.',
    long_description=open('README.rst').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-linkthru',
    download_url='http://github.com/powellc/django-linkthru/downloads',

    include_package_data=True,

    packages=['linkthru'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
