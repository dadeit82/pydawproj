"""Test module for DAWproject functionality."""

import tempfile
from pathlib import Path

from com.bitwig.dawproject.application import Application
from com.bitwig.dawproject.daw_project import DawProject
from com.bitwig.dawproject.double_adapter import double_to_string, string_to_double
from com.bitwig.dawproject.metadata import MetaData
from com.bitwig.dawproject.project import Project
from com.bitwig.dawproject.referenceable import Referenceable


def test_create_application():
    """Test creating an Application instance."""
    app = Application(name="TestApp", version="1.0.0")
    assert app.name == "TestApp"
    assert app.version == "1.0.0"


def test_create_metadata():
    """Test creating a MetaData instance."""
    metadata = MetaData()
    metadata.title = "Test Song"
    metadata.artist = "Test Artist"

    assert metadata.title == "Test Song"
    assert metadata.artist == "Test Artist"


def test_create_project():
    """Test creating a Project instance."""
    project = Project()
    project.application = Application(name="TestDAW", version="2.0.0")

    assert project.version == "1.0"
    assert project.application.name == "TestDAW"


def test_referenceable_auto_id():
    """Test the Referenceable auto-ID functionality."""
    # Test without auto-ID
    Referenceable.set_auto_id(False)
    ref1 = Referenceable()
    assert ref1.id is None

    # Test with auto-ID
    Referenceable.set_auto_id(True)
    ref2 = Referenceable()
    ref3 = Referenceable()
    assert ref2.id == "id1"
    assert ref3.id == "id2"


def test_double_adapter():
    """Test the double adapter for infinity constants."""
    # Test normal values
    assert string_to_double("1.5") == 1.5
    assert double_to_string(1.5) == "1.500000"

    # Test infinity
    assert string_to_double("inf") == float('inf')
    assert string_to_double("-inf") == float('-inf')
    assert double_to_string(float('inf')) == "inf"
    assert double_to_string(float('-inf')) == "-inf"

    # Test None/null
    assert string_to_double(None) is None
    assert string_to_double("null") is None
    assert double_to_string(None) is None


def test_save_and_load_project():
    """Test saving and loading a project."""
    # Create a dummy project
    project = Project()
    project.application = Application(name="TestApp", version="1.0")

    metadata = MetaData()
    metadata.title = "Test Project"

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "test.dawproject"

        # Save project
        DawProject.save(project, metadata, {}, file_path)
        assert file_path.exists()

        # Load project
        loaded_project = DawProject.load_project(file_path)
        assert loaded_project is not None

        # Load metadata
        loaded_metadata = DawProject.load_metadata(file_path)
        assert loaded_metadata is not None


def test_validate_project():
    """Test project validation."""
    project = Project()
    project.application = Application(name="ValidApp", version="1.0")

    # Should not raise an exception
    DawProject.validate(project)


if __name__ == "__main__":
    # Run all tests
    test_create_application()
    test_create_metadata()
    test_create_project()
    test_referenceable_auto_id()
    test_double_adapter()
    test_save_and_load_project()
    test_validate_project()
    print("All tests passed!")
