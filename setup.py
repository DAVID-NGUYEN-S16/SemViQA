from setuptools import setup, find_packages

setup(
    name="semviqa",
    version="1.1.6",
    packages=find_packages(),
    install_requires=[
        "transformers==4.42.3",
        "datasets==2.20.0",
        "pandas==2.2.2",
        "numpy==1.26.4",
        "underthesea==6.8.4",
        "gc-python-utils==0.0.1",
        "tqdm==4.66.4",
        "safetensors==0.4.3",
        "sentence-transformers==3.0.1",
        "scikit-learn==1.2.2",
        "matplotlib==3.7.5",
        "accelerate==0.32.1",
        "omegaconf==2.3.0",
        "einops==0.8.0",
        "rank_bm25==0.2.2",
        "sentencepiece==0.2.0",
        "pyvi==0.1.1",
    ],
    author="Nam V. Nguyen, Dien X. Tran, Thanh T. Tran, Anh T. Hoang, Tai V. Duong, Di T. Le, Phuc-Lu Le",
    author_email="xuandienk4@gmail.com",
    description="SemViQA: A Semantic Question Answering System for Vietnamese Fact-Checking",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DAVID-NGUYEN-S16/SemViQA",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    keywords="Vietnamese NLP, Fact-Checking, Question Answering, Machine Learning",
    project_urls={
        "Paper": "https://arxiv.org/abs/2503.00955",
        "Repository": "https://github.com/DAVID-NGUYEN-S16/SemViQA",
        "Competition Results": "https://codalab.lisn.upsaclay.fr/competitions/15497#results",
    },
)
