#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import setuptools

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='python_practice_automation_test_lib',
    python_requires=">=3.7",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['python_practice_automation_test_lib*']),
    include_package_data=True,
    package_data={"": ["*.properties"]},
    version='1.0',
    description='Web driver and API implement for Python Automation Practice Project',
    author='Phat Trinh',
    author_email='lowbudgetgaming001@gmail.com',
    url='https://github.com/trinhphat00101/python-practice-automation-test-lib',
    keywords=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: '
        'Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    install_requires=[
        'requests',
        'python-dotenv',
        'packaging'
    ],
)
