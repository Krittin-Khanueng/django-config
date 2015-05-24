from setuptools import setup, find_packages

version = '0.2.0'

packages = find_packages()

setup(
    name='dconfig',
    version=version,
    description='A Django config for the Django framework.',
    author='Shinz Natkid',
    author_email='shinznatkid@gmail.com',
    url='https://github.com/shinznatkid/django-config',
    packages=find_packages(),
    install_requires=[
        'django>=1.4.2',
        'pathlib>=1.0.0',
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
