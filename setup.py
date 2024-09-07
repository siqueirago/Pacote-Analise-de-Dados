from setuptools import setup, find_packages

setup(
    name="PacoteAnaliseDados",  # Nome do pacote
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Um pacote de exemplo para análise de dados.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Julio",
    author_email="seu.email@example.com",
    url="https://github.com/siqueirago/pacote-analise-dados",  # URL do projeto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)