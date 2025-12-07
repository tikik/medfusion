from setuptools import setup, find_packages

setup(
    name="medfusion",
    version="1.0.0",
    author="Trang Khong",
    author_email="your.email@example.com",
    description="Medical Multimodal VQA for Clinical Assistance",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/medfusion",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "pandas>=1.5.0",
        # ... same as requirements.txt
    ],
)
