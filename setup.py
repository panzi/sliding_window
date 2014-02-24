from distutils.core import setup

setup(name='sliding_window',
    author='Thomas Levine',
    author_email='_@thomaslevine.com',
    description='Move a window over an iterater (ngrams).',
    url='https://github.com/tlevine/moving_window.git',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['craigsgenerator'],
    install_requires = [],
    tests_require = ['nose'],
    version='0.0.1',
    license='AGPL'
)
