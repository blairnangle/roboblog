# RoboBlog

[![generate](https://github.com/blairnangle/roboblog/actions/workflows/generate.yml/badge.svg)](https://github.com/blairnangle/roboblog/actions/workflows/generate.yml)

Automated blog post writing using the Open AI API.

## Mechanism

1. Come up with a pseudorandom prompt—this should change frequently!
2. Use the Completions API to generate the body of the blog post
3. Use the `PyGithub` library to create a new blog post in the `blairnangle/blairnangle-dot-com` repo (to be displayed at [blairnangle.com/generative](https://blairnangle.com/generative)) with appropriate front matter and footer

## Usage

- Create a virtual environment:

```shell
python -m venv .venv
```
- Activate the virtual environment:

```shell
source .venv/bin/activate
```
- Install requirements:

```shell
pip install -r requirements.txt
```

- Export relevant authentication env vars:

```shell
export OPENAI_API_KEY=<insert Open AI API key>
export PERSONAL_ACCESS_TOKEN=<insert GitHub fine-grained personal access token>
```

- Go:

```shell
./go.py
```

## Authentication

### Wordnik

Apply for an API key (this can take a few days). Once it has been granted, save it as a GitHub
Secret named `WORDNIK_API_KEY`.

### Open AI

Generate an API key and saved it as a GitHub Secret named `OPENAI_API_KEY`.

Note that a paid Open AI account will be required once you are beyond the three-month free trial.

### GitHub

Create a fine-grained personal access token. The token needs to have the following permissions:

- Read access to metadata
- Read and Write access to code and commit statuses

Store the token as a GitHub Secret named `PERSONAL_ACCESS_TOKEN` (Secrets cannot have the `GITHUB_` prefix).
