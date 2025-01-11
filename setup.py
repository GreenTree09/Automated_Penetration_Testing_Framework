from setuptools import setup, find_packages

setup(
    name='automated_pen_test_framework',
    version='1.0.0',
    author='Satya',
    description='Automated Penetration Testing Framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        # more to come
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
    keywords='penetration testing security automation',
)
