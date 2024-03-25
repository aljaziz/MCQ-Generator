from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='1.0.0',
    author='aljaziz',
    author_email='turjatheharbingerofdeath@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2", "pandas"],
    packages=find_packages()
)