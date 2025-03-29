# Scanutils
Scanutils is a collection of utilities for processing scans of documents.

## Local installation

- Clone the repository and setup venv with uv then link executable to ~/.local/bin:
```bash
git clone https://github.com/stalbrec/scanutils.git
uv venv ~/.local/share/scanutils
source ~/.local/share/scanutils/bin/activate
uv pip install -e .
ln -s ~/.local/share/scanutils/bin/scanutils ~/.local/bin/scanutils
```