from pathlib import Path

import pandas as pd
import pytest

from starter_repo.plot_data import create_plot, read_csv_data


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Create a sample CSV file for testing."""
    df = pd.DataFrame({"x": [1.0, 2.0, 3.0, 4.0, 5.0], "y": [2.0, 4.0, 6.0, 8.0, 10.0]})
    file_path = tmp_path / "test.csv"
    df.to_csv(file_path, index=False)
    return file_path


def test_read_csv_data(sample_csv: Path) -> None:
    """Test reading data from CSV file."""
    x_data, y_data = read_csv_data(sample_csv, "x", "y")
    assert x_data == [1.0, 2.0, 3.0, 4.0, 5.0]
    assert y_data == [2.0, 4.0, 6.0, 8.0, 10.0]


def test_create_plot() -> None:
    """Test plot creation."""
    x_data = [1.0, 2.0, 3.0]
    y_data = [2.0, 4.0, 6.0]
    fig = create_plot(x_data, y_data, "X", "Y", "Test Plot")
    assert fig is not None
    # Basic check that the figure contains the expected elements
    ax = fig.axes[0]
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_title() == "Test Plot"
