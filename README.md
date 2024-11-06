# cdk-knowledge-extractor

> [!WARNING]
> This project is experimental.

Extract integ test code in aws/aws-cdk repo to use as a knowledge base. Test code stored in markdown to use with Amazon Bedrock Knowledge Bases.

## Requirements

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/)
  - via [pypa/pipx](https://github.com/pypa/pipx)

On Linux:

```sh
sudo apt update
sudo apt install pipx
pipx ensurepath
pipx install poetry
```

On macOS:

```sh
brew install pipx
pipx ensurepath
pipx install poetry
```

## Usage

Setup and install dependencies:

```sh
git clone https://github.com/konokenj/cdk-knowledge-extractor.git
poetry install
```

Generate markdown files:

```sh
poetry run python -m cdk_knowledge_extractor
```

Upload to S3:

```sh
aws s3 sync dist/ s3://sample-bucket/integ-tests
```

## Contributing

```sh
# Update project files and install dependencies
poetry run projen
# Run unit tests
poetry run pytest -s tests/
```
