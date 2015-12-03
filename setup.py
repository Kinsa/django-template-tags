from setuptools import setup, find_packages


setup(
    name='django-templatetags',
    version='1.1.0',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'beautifulsoup4>=4.0',
        'Django>=1.7'
    ],
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    description="Set of 'generic' templatetags for Django",
    url='https://github.com/jbergantine/django-robots',
    download_url='https://github.com/jbergantine/django-templatetags/tarball/1.1.0',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
