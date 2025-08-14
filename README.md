# Python Project Starter Repository

This repository serves as a template demonstrating Python best practices for research projects. It includes:

- An example Python program (reading in data and plotting)
- Command-line argument parsing ([argparse](https://docs.python.org/3/library/argparse.html))
- Code style checking, aka "linting" (with [ruff](https://github.com/astral-sh/ruff))
- Static type checking (with [mypy](https://mypy.readthedocs.io/))
- Pre-commit hooks that run these checks automatically (with [pre-commit](https://pre-commit.com/))
- Testing (with [pytest](https://docs.pytest.org/))
- Continuous Integration (with [GitHub Actions](https://github.com/features/actions))
- Package management (with [pip](https://pip.pypa.io/) and [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/))
- An open source license ([MIT](https://opensource.org/licenses/MIT))

## Features

### 1. Data Processing and Visualization

The main script ([starter_repo/plot_data.py](starter_repo/plot_data.py)) can be replaced with any code that you want to write.

Installation can be done as follows:

```bash
# Install the package
pip install .

# Create a plot from the sample data
python -m starter_repo.plot_data data/sample.csv year population --title "Population Growth" -o population.png
```

### 2. Testing

Writing unit tests is a good way to ensure that your code behaves as expected, and you can write unit tests before you write the code that you want to test (aka "test-driven development"). Test files are located in the [tests/](tests/) directory.

To run tests:

```bash
pip install ".[dev]"  # Install development dependencies
pytest
```

### 3. Code Quality Tools

This project uses several tools to maintain code quality:

#### Pre-commit Hooks

We use [pre-commit](.pre-commit-config.yaml) with:

- [Ruff](https://github.com/charliermarsh/ruff) for linting and formatting
- [mypy](https://mypy.readthedocs.io/) for static type checking

To set up pre-commit:

```bash
pip install pre-commit
pre-commit install
```

### 4. Continuous Integration

GitHub Actions workflows are set up for:

- [Linting](.github/workflows/lint.yml): Runs pre-commit hooks (Ruff and mypy)
- [Testing](.github/workflows/test.yml): Runs pytest on multiple Python versions


## Contributing

1. Fork the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Install pre-commit hooks: `pre-commit install`
4. Make your changes
5. Run tests: `pytest`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

> **Note**: Without a license, the code is under exclusive copyright by default. This means no one can copy, distribute, or modify your work without facing potential legal consequences. Adding a license (like MIT) explicitly grants these permissions, making it clear how others can use your code.

## Citation

This was created by [Graham Neubig](https://phontron.com) primarily as an example for student researchers.

One final thing: when you publish your research code, it's good to add a BibTeX entry like this to the paper (or just the repo) so people can cite it easily:

```bibtex
@misc{neubig2025starter,
  author = {Graham Neubig},
  title = {Python Project Starter Repository},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/neubig/starter-repo}}
}
```
