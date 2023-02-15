@ECHO OFF
if exist .venv (
    echo "virtual environment exists!"
) else (
    echo "Creating virtual environment!"
    python -m venv .venv
)

if exist .venv (
    echo "Saving changes and build new wheels"
    .\.venv\Scripts\activate.bat

    pip install build 
    if exist dist (
        echo "Adding/updating .whl file!"
        python3 -m build --wheel
    ) else (
        echo "Creating distribution folder!"
        python3 -m build --sdist
    )     
)
