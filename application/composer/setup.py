from setuptools import setup, find_packages

setup(
    name='composer',
    version='0.0.1',
    url='https://gitlab.com/problemfighter/goods-mama-backend.git',
    license='Problem Fighter License',
    author='composer',
    author_email='codegen@problemfighter.com',
    description='',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)