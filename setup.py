from setuptools import setup, find_packages

setup(
    name='automated_pen_test_framework',
    version='1.0.0',
    author='Satya',
    description='Automated Penetration Testing Framework',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        # more  to come
    ],
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md'],
    },
    entry_points={
        'console_scripts': [
            'pen-test=src.vulnerability_assessment.assessor:main',
        ],
    },
)