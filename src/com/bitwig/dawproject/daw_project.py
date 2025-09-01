"""Several helper functions to deal with DAWproject files."""

import json
import zipfile
from pathlib import Path

from .metadata import MetaData
from .project import Project


class DawProject:
    """Several helper functions to deal with DAWproject files."""

    FORMAT_NAME = "DAWproject exchange format"
    """The (English) description text of the format."""

    FILE_EXTENSION = "dawproject"
    """The file extension for DAWproject files."""

    _PROJECT_FILE = "project.xml"
    _METADATA_FILE = "metadata.xml"

    @staticmethod
    def save_xml(project: Project, file_path: Path) -> None:
        """Store the given project to the given file.

        Args:
            project: The project to store
            file_path: The file into which to store the project

        Raises:
            IOError: Could not store the project
        """
        project_xml = DawProject._to_xml(project)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(project_xml)

    @staticmethod
    def save(
        project: Project,
        metadata: MetaData,
        embedded_files: dict[Path, str],
        file_path: Path,
    ) -> None:
        """Store the given project, metadata and embedded files to the given (ZIP) file.

        Args:
            project: The project to store
            metadata: The metadata to store
            embedded_files: The embedded files (source_path -> zip_path)
            file_path: The file into which to store the project

        Raises:
            IOError: Could not store the files
        """
        metadata_xml = DawProject._to_xml(metadata)
        project_xml = DawProject._to_xml(project)

        with zipfile.ZipFile(file_path, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(DawProject._METADATA_FILE, metadata_xml.encode("utf-8"))
            zf.writestr(DawProject._PROJECT_FILE, project_xml.encode("utf-8"))

            for source_file, zip_path in embedded_files.items():
                zf.write(source_file, zip_path)

    @staticmethod
    def load_project(file_path: Path) -> Project:
        """Load a project from the given file.

        Args:
            file_path: The file which contains the project in ZIP format

        Returns:
            The loaded project

        Raises:
            IOError: Could not load the project
        """
        with zipfile.ZipFile(file_path, "r") as zf:
            with zf.open(DawProject._PROJECT_FILE) as f:
                xml_data = f.read().decode("utf-8")
                return DawProject._from_xml(xml_data, Project)

    @staticmethod
    def load_metadata(file_path: Path) -> MetaData:
        """Load metadata from the given file.

        Args:
            file_path: The file which contains the metadata in ZIP format

        Returns:
            The loaded metadata

        Raises:
            IOError: Could not load the metadata
        """
        with zipfile.ZipFile(file_path, "r") as zf:
            with zf.open(DawProject._METADATA_FILE) as f:
                xml_data = f.read().decode("utf-8")
                return DawProject._from_xml(xml_data, MetaData)

    @staticmethod
    def load_embedded(file_path: Path, embedded_path: str) -> bytes:
        """Load the data of an embedded file.

        Args:
            file_path: The ZIP archive which contains the embedded file
            embedded_path: The path of the embedded file in the ZIP archive

        Returns:
            The loaded data

        Raises:
            IOError: Could not load the embedded file
        """
        with zipfile.ZipFile(file_path, "r") as zf:
            with zf.open(embedded_path) as f:
                return f.read()

    @staticmethod
    def validate(project: Project) -> None:
        """Validate the given project by serializing it to XML.

        Args:
            project: The project to validate

        Raises:
            IOError: Error validating the project
        """
        # For now, just try to serialize - a more complete implementation
        # would validate against an XML schema
        try:
            DawProject._to_xml(project)
        except Exception as e:
            raise OSError(f"Project validation failed: {e}") from e

    @staticmethod
    def _to_xml(obj) -> str:
        """Convert an object to XML representation.

        This is a simplified implementation - a complete version would use
        proper XML serialization matching the Java JAXB annotations.
        """
        # For now, return a simple JSON representation as placeholder
        # A complete implementation would convert the dataclass to proper XML
        from dataclasses import asdict
        data = asdict(obj) if hasattr(obj, '__dataclass_fields__') else vars(obj)
        return (
            f"<!-- XML representation of {type(obj).__name__} -->\n"
            f"{json.dumps(data, indent=2)}"
        )

    @staticmethod
    def _from_xml(xml_data: str, cls):
        """Convert XML data to an object instance.

        This is a simplified implementation - a complete version would use
        proper XML deserialization matching the Java JAXB annotations.
        """
        # For now, create a basic instance
        # A complete implementation would parse the XML and populate the object
        return cls()
