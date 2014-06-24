from setuptools import setup

setup(
    name = 'labgeeks-apollo',
    version = '1.0',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks-apollo',
    description = 'Consultant forms and tools app for the labgeeks suite of student staff management tools.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_apollo',],
    install_requires = [
        'setuptools',
        'pillow',
        'South==0.7.3',
        'django-forms-builder==0.9',
    ],
)
