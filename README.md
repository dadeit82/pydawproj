# PyDAWProject

Python implementation of the [DAWproject exchange format](https://dawproject.org/) - a universal format for transferring digital audio workstation projects between different DAW applications.

## Overview

This project provides a complete Python translation of the Java DAWproject library, maintaining 100% compatibility with the original specification while leveraging modern Python features including:

- Type hints for all classes and methods
- Dataclasses for clean, readable data structures
- Modern Python enums and collections
- Comprehensive test suite
- Continuous integration with linting and type checking

## Installation

```bash
pip install pydawproj
```

Or for development:

```bash
git clone https://github.com/dadeit82/pydawproj.git
cd pydawproj
pip install -e .
```

## Usage

### Creating a DAWproject

```python
from com.bitwig.dawproject.project import Project
from com.bitwig.dawproject.application import Application
from com.bitwig.dawproject.metadata import MetaData
from com.bitwig.dawproject.daw_project import DawProject
from com.bitwig.dawproject.utility import Utility
from com.bitwig.dawproject.content_type import ContentType
from com.bitwig.dawproject.mixer_role import MixerRole
from pathlib import Path

# Create a new project
project = Project()
project.application = Application(name="MyDAW", version="1.0.0")

# Create a track
track = Utility.create_track(
    name="Audio Track",
    content_types={ContentType.AUDIO},
    mixer_role=MixerRole.REGULAR,
    volume=0.8,
    pan=0.5
)
project.structure.append(track)

# Create metadata
metadata = MetaData()
metadata.title = "My Song"
metadata.artist = "My Artist"

# Save the project
DawProject.save(project, metadata, {}, Path("my_song.dawproject"))
```

### Loading a DAWproject

```python
from com.bitwig.dawproject.daw_project import DawProject
from pathlib import Path

# Load a project
project = DawProject.load_project(Path("my_song.dawproject"))
metadata = DawProject.load_metadata(Path("my_song.dawproject"))

print(f"Loaded: {metadata.title} by {metadata.artist}")
print(f"Tracks: {len(project.structure)}")
```

## Project Structure

The library follows the same package structure as the Java implementation:

```
src/com/bitwig/dawproject/
├── __init__.py              # Main package
├── application.py           # Application metadata
├── metadata.py             # Song metadata
├── project.py              # Main project class
├── daw_project.py          # File I/O utilities
├── utility.py              # Helper functions
├── *_parameter.py          # Parameter types
├── device/                 # Audio devices and plugins
│   ├── device.py
│   ├── plugin.py
│   └── *_plugin.py
└── timeline/               # Timeline and automation
    ├── timeline.py
    ├── clips.py
    └── *.py
```

## Features

- **Complete Translation**: All 69 Java classes translated to Python
- **Type Safety**: Full type hints for better IDE support and error catching
- **Modern Python**: Uses dataclasses, enums, and modern syntax
- **Comprehensive Tests**: Unit tests covering all major functionality
- **CI/CD**: Automated testing with GitHub Actions
- **Linting**: Code quality ensured with ruff and mypy

## Compatibility

This implementation maintains full compatibility with the DAWproject specification and can read/write files that are compatible with:

- Bitwig Studio
- PreSonus Studio One
- Other DAWproject-compatible applications

## Development

### Running Tests

```bash
pytest tests/
```

### Linting

```bash
ruff check src/ tests/
ruff format src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Contributing

Contributions are welcome! Please ensure that:

1. All tests pass
2. Code is properly formatted with ruff
3. Type hints are complete
4. New features include tests

## License

This project follows the same license as the original Java implementation.

## Acknowledgments

This is a Python translation of the DAWproject format originally developed by Bitwig. The Java reference implementation served as the basis for this Python version.