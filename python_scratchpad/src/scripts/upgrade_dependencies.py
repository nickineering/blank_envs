import subprocess
from pathlib import Path

import toml

# ruff: noqa:S603,S607


def upgrade_dependencies() -> None:
    # Load pyproject.toml
    with Path("pyproject.toml").open("r") as file:
        pyproject = toml.load(file)

    # Extract dependencies
    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    dev_dependencies = pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"]

    # Update each dependency to the latest version
    for dep in dependencies:
        if dep != "python":  # Skip python version
            _ = subprocess.run(["poetry", "add", f"{dep}@latest"], check=False)

    for dev_dep in dev_dependencies:
        _ = subprocess.run(
            ["poetry", "add", "--group", "dev", f"{dev_dep}@latest"], check=False
        )


if __name__ == "__main__":
    upgrade_dependencies()
