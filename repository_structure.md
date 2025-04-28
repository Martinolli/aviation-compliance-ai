# Aviation Compliance AI Repository Structure

## Repository Name Suggestions

- `aviation-compliance-ai`
- `aero-compliance-assistant`
- `skyregs-ai`
- `aviation-regulatory-assistant`
- `compliance-navigator-ai`

## Directory Structure

```bash
aviation-compliance-ai/
├── .github/                      # GitHub workflows and templates
│   ├── workflows/                # CI/CD pipeline configurations
│   └── ISSUE_TEMPLATE/           # Issue templates
├── src/                          # Source code
│   ├── core/                     # Core functionality
│   │   ├── config/               # Configuration management
│   │   ├── logging/              # Logging utilities
│   │   ├── exceptions/           # Custom exception classes
│   │   └── utils/                # Utility functions
│   ├── data/                     # Data processing
│   │   ├── readers/              # Document readers for different formats
│   │   ├── processors/           # Text processing and cleaning
│   │   ├── chunkers/             # Document chunking strategies
│   │   └── extractors/           # Metadata and entity extraction
│   ├── embeddings/               # Embedding generation and management
│   │   ├── models/               # Embedding model interfaces
│   │   ├── generators/           # Embedding generation logic
│   │   └── optimizers/           # Embedding optimization utilities
│   ├── storage/                  # Data storage interfaces
│   │   ├── vector_db/            # Vector database adapters
│   │   ├── document_store/       # Document storage adapters
│   │   └── cache/                # Caching mechanisms
│   ├── retrieval/                # Retrieval mechanisms
│   │   ├── engines/              # Search engine implementations
│   │   ├── rankers/              # Result ranking algorithms
│   │   └── filters/              # Query and result filters
│   ├── generation/               # Response generation
│   │   ├── prompts/              # Prompt templates and management
│   │   ├── validators/           # Response validation
│   │   └── formatters/           # Response formatting
│   ├── knowledge/                # Domain-specific knowledge
│   │   ├── regulatory/           # Regulatory framework models
│   │   │   ├── faa/              # FAA regulations
│   │   │   └── easa/             # EASA regulations
│   │   ├── safety/               # Safety analysis frameworks
│   │   │   ├── hfacs/            # Human Factors Analysis
│   │   │   └── accidents/        # Accident analysis
│   │   └── aviation/             # Aviation-specific knowledge
│   ├── api/                      # API interfaces
│   │   ├── rest/                 # REST API implementation
│   │   └── websocket/            # WebSocket implementation
│   └── ui/                       # User interface components
│       ├── web/                  # Web interface
│       │   ├── components/       # Reusable UI components
│       │   ├── pages/            # Page definitions
│       │   ├── styles/           # CSS/SCSS styles
│       │   └── utils/            # Frontend utilities
│       └── cli/                  # Command-line interface
├── scripts/                      # Utility scripts
│   ├── setup/                    # Setup scripts
│   ├── data/                     # Data processing scripts
│   └── deployment/               # Deployment scripts
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── fixtures/                 # Test fixtures
├── docs/                         # Documentation
│   ├── architecture/             # Architecture documentation
│   ├── api/                      # API documentation
│   ├── user/                     # User guides
│   └── developer/                # Developer guides
├── config/                       # Configuration files
│   ├── development/              # Development environment configs
│   ├── testing/                  # Testing environment configs
│   └── production/               # Production environment configs
├── data/                         # Data directory
│   ├── raw/                      # Raw document storage
│   │   ├── faa/                  # FAA documents
│   │   ├── easa/                 # EASA documents
│   │   └── accidents/            # Accident reports
│   ├── processed/                # Processed documents
│   ├── embeddings/               # Generated embeddings
│   └── regulatory/               # Regulatory document storage
├── .env.example                  # Example environment variables
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
├── package.json                  # JavaScript dependencies
├── README.md                     # Project overview
└── LICENSE                       # License information
```

## Initial Files to Create

### 1. Project Configuration Files

#### `.env.example`

```batch
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key

# AstraDB Configuration
ASTRA_DB_SECURE_BUNDLE_PATH=path/to/secure-connect-bundle.zip
ASTRA_DB_CLIENT_ID=your_client_id
ASTRA_DB_CLIENT_SECRET=your_client_secret
ASTRA_DB_KEYSPACE=your_keyspace

# Application Configuration
DATA_DIR=./data
LOG_LEVEL=INFO
```

#### `requirements.txt`

```batch
# Core dependencies
python-dotenv>=0.19.0
pydantic>=1.9.0
loguru>=0.6.0

# Document processing
pdfplumber>=0.7.0
python-docx>=0.8.11
spacy>=3.2.0
nltk>=3.6.0
beautifulsoup4>=4.10.0

# NLP and embeddings
openai>=1.0.0
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0
tiktoken>=0.3.0

# Vector database
faiss-cpu>=1.7.0
cassandra-driver>=3.25.0

# Web and API
fastapi>=0.68.0
uvicorn>=0.15.0
websockets>=10.0
httpx>=0.23.0

# Testing
pytest>=6.2.5
pytest-cov>=2.12.0

# Utilities
tqdm>=4.62.0
```

#### `package.json`

```json
{
  "name": "aviation-compliance-ai",
  "version": "0.1.0",
  "description": "Aviation Compliance AI Assistant",
  "scripts": {
    "start": "node src/ui/web/server.js",
    "dev": "nodemon src/ui/web/server.js",
    "test": "jest"
  },
  "dependencies": {
    "openai": "^4.0.0",
    "cassandra-driver": "^4.6.0",
    "dotenv": "^10.0.0",
    "express": "^4.17.1",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^0.24.0"
  },
  "devDependencies": {
    "jest": "^27.0.0",
    "nodemon": "^2.0.15",
    "eslint": "^8.0.0"
  }
}
```

#### `README.md`

```markdown
# Aviation Compliance AI

An intelligent assistant for aviation compliance, focusing on FAA and EASA regulations for design organization certification and project certification, with integrated accident analysis capabilities.

## Features

- Regulatory information retrieval for FAA and EASA regulations
- Cross-reference between different regulatory frameworks
- Accident analysis and lessons learned integration
- Compliance verification tools
- User-friendly interface for aviation professionals

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 16+
- OpenAI API key
- AstraDB account (or alternative vector database)

### Installation

1.Clone the repository

   ```batch
   git clone https://github.com/yourusername/aviation-compliance-ai.git
   cd aviation-compliance-ai
   ```

2.Install Python dependencies

   ```batch
   pip install -r requirements.txt
   ```

3.Install JavaScript dependencies

   ```batch
   npm install
   ```

4.Copy the example environment file and update with your credentials

   ```batch
   cp .env.example .env
   ```

5.Run the setup script

   ```batch
   python scripts/setup/initial_setup.py
   ```

## Usage

### Processing Documents

```python
python scripts/data/process_documents.py --source data/raw/faa --output data/processed/faa
```

### Generating Embeddings

```python
python scripts/data/generate_embeddings.py --source data/processed/faa --output data/embeddings/faa
```

### Running the Web Interface

```python
npm run start
```

## Development

### Running Tests

```python
pytest tests/
```

### Code Style

This project follows PEP 8 for Python code and Airbnb style guide for JavaScript.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```batch

### 2. Core Module Files

#### `src/core/config/config.py`

```python
"""Configuration management for Aviation Compliance AI."""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration manager for the application."""
    
    _instance = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """Load configuration from files and environment variables."""
        # Determine environment
        env = os.getenv("ENVIRONMENT", "development")
        
        # Base paths
        base_dir = Path(__file__).parent.parent.parent.parent
        config_dir = base_dir / "config"
        
        # Load default config
        default_config_path = config_dir / "default.yaml"
        if default_config_path.exists():
            with open(default_config_path, "r") as f:
                self._config = yaml.safe_load(f)
        
        # Load environment-specific config
        env_config_path = config_dir / f"{env}.yaml"
        if env_config_path.exists():
            with open(env_config_path, "r") as f:
                env_config = yaml.safe_load(f)
                self._deep_update(self._config, env_config)
        
        # Override with environment variables
        self._override_from_env()
    
    def _deep_update(self, d: Dict[str, Any], u: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively update a dictionary."""
        for k, v in u.items():
            if isinstance(v, dict) and k in d and isinstance(d[k], dict):
                self._deep_update(d[k], v)
            else:
                d[k] = v
        return d
    
    def _override_from_env(self):
        """Override configuration with environment variables."""
        # Example: OPENAI_API_KEY -> openai.api_key
        if os.getenv("OPENAI_API_KEY"):
            if "openai" not in self._config:
                self._config["openai"] = {}
            self._config["openai"]["api_key"] = os.getenv("OPENAI_API_KEY")
        
        # Example: ASTRA_DB_CLIENT_ID -> astra.client_id
        if os.getenv("ASTRA_DB_CLIENT_ID"):
            if "astra" not in self._config:
                self._config["astra"] = {}
            self._config["astra"]["client_id"] = os.getenv("ASTRA_DB_CLIENT_ID")
        
        if os.getenv("ASTRA_DB_CLIENT_SECRET"):
            if "astra" not in self._config:
                self._config["astra"] = {}
            self._config["astra"]["client_secret"] = os.getenv("ASTRA_DB_CLIENT_SECRET")
        
        if os.getenv("ASTRA_DB_SECURE_BUNDLE_PATH"):
            if "astra" not in self._config:
                self._config["astra"] = {}
            self._config["astra"]["secure_bundle_path"] = os.getenv("ASTRA_DB_SECURE_BUNDLE_PATH")
        
        if os.getenv("ASTRA_DB_KEYSPACE"):
            if "astra" not in self._config:
                self._config["astra"] = {}
            self._config["astra"]["keyspace"] = os.getenv("ASTRA_DB_KEYSPACE")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        keys = key.split(".")
        config = self._config
        for i, k in enumerate(keys[:-1]):
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value

# Create a singleton instance
config = Config()
```

### `src/core/logging/logger.py`

```python
"""Logging configuration for Aviation Compliance AI."""

import os
import sys
from pathlib import Path
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

from ..config.config import config

class Logger:
    """Logger configuration for the application."""
    
    _instance = None
    _loggers = {}
    
    def __new__(cls):
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._configure_logging()
        return cls._instance
    
    def _configure_logging(self):
        """Configure logging with file and console handlers."""
        # Determine log directory
        base_dir = Path(__file__).parent.parent.parent.parent
        log_dir = base_dir / "logs"
        log_dir.mkdir(exist_ok=True)
        
        # Create timestamp for log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"aviation_compliance_{timestamp}.log"
        
        # Get log level from config
        log_level_str = config.get("logging.level", "INFO")
        log_level = getattr(logging, log_level_str.upper())
        
        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        # Create file handler
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=10*1024*1024,  # 10 MB
            backupCount=5
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        
        # Configure root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)
        
        # Remove existing handlers to avoid duplicates
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
            
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
        
        # Suppress verbose logging from libraries
        logging.getLogger("openai").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        
        # Store root logger
        self._loggers["root"] = root_logger
    
    def get_logger(self, name: str = None) -> logging.Logger:
        """Get a logger instance."""
        if name is None:
            return self._loggers["root"]
        
        if name not in self._loggers:
            self._loggers[name] = logging.getLogger(name)
        
        return self._loggers[name]

# Create a singleton instance
logger_manager = Logger()

def get_logger(name: str = None) -> logging.Logger:
    """Get a logger instance."""
    return logger_manager.get_logger(name)
```

### `src/core/exceptions/exceptions.py`

```python
"""Custom exceptions for Aviation Compliance AI."""

class AviationComplianceError(Exception):
    """Base exception for all Aviation Compliance AI errors."""
    pass

class ConfigurationError(AviationComplianceError):
    """Error in configuration."""
    pass

class DocumentProcessingError(AviationComplianceError):
    """Error in document processing."""
    pass

class EmbeddingError(AviationComplianceError):
    """Error in embedding generation or management."""
    pass

class StorageError(AviationComplianceError):
    """Error in data storage operations."""
    pass

class RetrievalError(AviationComplianceError):
    """Error in retrieval operations."""
    pass

class GenerationError(AviationComplianceError):
    """Error in response generation."""
    pass

class RegulatoryError(AviationComplianceError):
    """Error in regulatory processing."""
    pass

class AccidentAnalysisError(AviationComplianceError):
    """Error in accident analysis."""
    pass

class APIError(AviationComplianceError):
    """Error in API operations."""
    pass

class UIError(AviationComplianceError):
    """Error in UI operations."""
    pass
```

### 3. Document Processing Files

### `src/data/readers/base_reader.py`

```python
"""Base document reader interface."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional

class BaseReader(ABC):
    """Base interface for document readers."""
    
    @abstractmethod
    def read(self, file_path: str) -> Dict[str, Any]:
        """
        Read a document and return its content and metadata.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Dictionary containing:
                - text: Extracted text content
                - metadata: Document metadata
        """
        pass
    
    def supports(self, file_path: str) -> bool:
        """
        Check if this reader supports the given file type.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            True if this reader supports the file type, False otherwise
        """
        return False
    
    def _get_file_extension(self, file_path: str) -> str:
        """
        Get the file extension from a file path.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            File extension (lowercase, without the dot)
        """
        return Path(file_path).suffix.lower()[1:]
```

### `src/data/readers/docx_reader.py`

```python
"""DOCX document reader."""

import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import docx
from datetime import datetime

from .base_reader import BaseReader
from ...core.exceptions.exceptions import DocumentProcessingError
from ...core.logging.logger import get_logger

logger = get_logger(__name__)

class DocxReader(BaseReader):
    """Reader for DOCX documents."""
    
    def supports(self, file_path: str) -> bool:
        """Check if this reader supports the given file type."""
        return self._get_file_extension(file_path) == "docx"
    
    def read(self, file_path: str) -> Dict[str, Any]:
        """Read a DOCX document and return its content and metadata."""
        try:
            logger.info(f"Reading DOCX document: {file_path}")
            
            # Check if file exists
            if not os.path.exists(file_path):
                raise DocumentProcessingError(f"File not found: {file_path}")
            
            # Open the document
            doc = docx.Document(file_path)
            
            # Extract text
            paragraphs = []
            for para in doc.paragraphs:
                if para.text.strip():  # Skip empty paragraphs
                    paragraphs.append(para.text)
            
            # Extract text from tables
            for table in doc.tables:
                for row in table.rows:
                    row_text = []
                    for cell in row.cells:
                        if cell.text.strip():  # Skip empty cells
                            row_text.append(cell.text.strip())
                    if row_text:
                        paragraphs.append(" | ".join(row_text))
            
            # Join paragraphs with newlines
            text = "\n\n".join(paragraphs)
            
            # Extract metadata
            metadata = self._extract_metadata(doc, file_path)
            
            logger.info(f"Successfully read DOCX document: {file_path}")
            return {
                "text": text,
                "metadata": metadata
            }
            
        except Exception as e:
            logger.error(f"Error reading DOCX document {file_path}: {str(e)}")
            raise DocumentProcessingError(f"Error reading DOCX document: {str(e)}")
    
    def _extract_metadata(self, doc: docx.Document, file_path: str) -> Dict[str, Any]:
        """Extract metadata from a DOCX document."""
        metadata = {}
        
        # File metadata
        file_path_obj = Path(file_path)
        metadata["filename"] = file_path_obj.name
        metadata["file_extension"] = "docx"
        metadata["file_path"] = str(file_path_obj.absolute())
        metadata["file_size"] = file_path_obj.stat().st_size
        metadata["last_modified"] = datetime.fromtimestamp(
            file_path_obj.stat().st_mtime
        ).isoformat()
        
        # Document properties
        try:
            core_properties = doc.core_properties
            metadata["title"] = core_properties.title if core_properties.title else ""
            metadata["author"] = core_properties.author if core_properties.author else ""
            metadata["created"] = core_properties.created.isoformat() if core_properties.created else ""
            metadata["modified"] = core_properties.modified.isoformat() if core_properties.modified else ""
            metadata["last_modified_by"] = core_properties.last_modified_by if core_properties.last_modified_by else ""
            metadata["revision"] = core_properties.revision if core_properties.revision else ""
            metadata["category"] = core_properties.category if core_properties.category else ""
            metadata["comments"] = core_properties.comments if core_properties.comments else ""
            metadata["subject"] = core_properties.subject if core_properties.subject else ""
            metadata["keywords"] = core_properties.keywords if core_properties.keywords else ""
        except Exception as e:
            logger.warning(f"Error extracting core properties from {file_path}: {str(e)}")
        
        # Document statistics
        metadata["paragraph_count"] = len(doc.paragraphs)
        metadata["table_count"] = len(doc.tables)
        metadata["section_count"] = len(doc.sections)
        
        # Try to extract document type from content or filename
        metadata["document_type"] = self._guess_document_type(doc, file_path_obj.name)
        
        return metadata
    
    def _guess_document_type(self, doc: docx.Document, filename: str) -> str:
        """Guess the document type based on content and filename."""
        # Check first few paragraphs for type indicators
        first_paragraphs = " ".join([p.text for p in doc.paragraphs[:10] if p.text.strip()])
        
        # Check for regulatory document indicators
        if any(term in first_paragraphs.lower() for term in ["regulation", "directive", "advisory", "circular", "order"]):
            return "regulatory"
        
        # Check for accident report indicators
        if any(term in first_paragraphs.lower() for term in ["accident", "incident", "investigation", "safety report"]):
            return "accident_report"
        
        # Check for manual indicators
        if any(term in first_paragraphs.lower() for term in ["manual", "handbook", "guide", "procedure"]):
            return "manual"
        
        # Check filename for indicators
        filename_lower = filename.lower()
        if any(term in filename_lower for term in ["faa", "easa", "regulation", "part", "advisory"]):
            return "regulatory"
        if any(term in filename_lower for term in ["accident", "incident", "investigation", "safety"]):
            return "accident_report"
        if any(term in filename_lower for term in ["manual", "handbook", "guide", "procedure"]):
            return "manual"
        
        # Default
        return "unknown"
```

### 4. Setup Script

### `scripts/setup/initial_setup.py`

```python
#!/usr/bin/env python3
"""
Initial setup script for Aviation Compliance AI.

This script:
1. Creates necessary directories
2. Initializes configuration files
3. Checks dependencies
4. Sets up initial database structure
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import yaml
import pkg_resources

def print_header(message):
    """Print a formatted header message."""
    print("\n" + "=" * 80)
    print(f" {message}")
    print("=" * 80)

def create_directories():
    """Create necessary directories if they don't exist."""
    print_header("Creating Directories")
    
    # Get base directory (project root)
    base_dir = Path(__file__).parent.parent.parent
    
    # Directories to create
    directories = [
        base_dir / "data" / "raw" / "faa",
        base_dir / "data" / "raw" / "easa",
        base_dir / "data" / "raw" / "accidents",
        base_dir / "data" / "processed",
        base_dir / "data" / "embeddings",
        base_dir / "data" / "regulatory",
        base_dir / "logs",
        base_dir / "config" / "development",
        base_dir / "config" / "testing",
        base_dir / "config" / "production",
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def create_config_files():
    """Create initial configuration files."""
    print_header("Creating Configuration Files")
    
    # Get base directory (project root)
    base_dir = Path(__file__).parent.parent.parent
    
    # Default configuration
    default_config = {
        "application": {
            "name": "Aviation Compliance AI",
            "version": "0.1.0"
        },
        "paths": {
            "data": str(base_dir / "data"),
            "raw": "${paths.data}/raw",
            "processed": "${paths.data}/processed",
            "embeddings": "${paths.data}/embeddings",
            "regulatory": "${paths.data}/regulatory",
            "logs": str(base_dir / "logs")
        },
        "embedding": {
            "model": "text-embedding-ada-002",
            "dimensions": 1536,
            "batch_size": 10,
            "max_retries": 3,
            "retry_delay": 1000
        },
        "retrieval": {
            "k": 20,
            "max_tokens": 6000,
            "min_similarity": 0.7
        },
        "generation": {
            "model": "gpt-4-turbo",
            "temperature": 0.6,
            "max_tokens": 2000
        },
        "logging": {
            "level": "INFO",
            "file_rotation": 5,
            "file_max_size": 10485760  # 10 MB
        }
    }
    
    # Development configuration
    dev_config = {
        "logging": {
            "level": "DEBUG"
        }
    }
    
    # Testing configuration
    test_config = {
        "logging": {
            "level": "DEBUG"
        },
        "embedding": {
            "batch_size": 5
        }
    }
    
    # Production configuration
    prod_config = {
        "logging": {
            "level": "INFO"
        }
    }
    
    # Write configuration files
    config_files = [
        (base_dir / "config" / "default.yaml", default_config),
        (base_dir / "config" / "development" / "config.yaml", dev_config),
        (base_dir / "config" / "testing" / "config.yaml", test_config),
        (base_dir / "config" / "production" / "config.yaml", prod_config)
    ]
    
    for file_path, config in config_files:
        with open(file_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
        print(f"✓ Created configuration file: {file_path}")

def check_dependencies():
    """Check if all required dependencies are installed."""
    print_header("Checking Dependencies")
    
    # Get base directory (project root)
    base_dir = Path(__file__).parent.parent.parent
    
    # Check Python dependencies
    requirements_file = base_dir / "requirements.txt"
    if requirements_file.exists():
        with open(requirements_file, "r") as f:
            requirements = [
                line.strip().split(">=")[0].split("==")[0]
                for line in f.readlines()
                if line.strip() and not line.startswith("#")
            ]
        
        missing_packages = []
        for package in requirements:
            try:
                pkg_resources.get_distribution(package)
                print(f"✓ Found package: {package}")
            except pkg_resources.DistributionNotFound:
                missing_packages.append(package)
                print(f"✗ Missing package: {package}")
        
        if missing_packages:
            print("\nSome required packages are missing. Install them with:")
            print(f"pip install -r {requirements_file}")
    else:
        print("✗ requirements.txt not found")
    
    # Check Node.js dependencies if package.json exists
    package_json = base_dir / "package.json"
    if package_json.exists() and shutil.which("npm"):
        try:
            subprocess.run(["npm", "list", "--depth=0"], cwd=base_dir, check=False)
        except subprocess.SubprocessError:
            print("\nSome Node.js dependencies may be missing. Install them with:")
            print("npm install")
    elif package_json.exists():
        print("✗ package.json found but npm is not installed")
    else:
        print("✗ package.json not found")

def check_environment_variables():
    """Check if required environment variables are set."""
    print_header("Checking Environment Variables")
    
    # Required environment variables
    required_vars = [
        "OPENAI_API_KEY",
        "ASTRA_DB_CLIENT_ID",
        "ASTRA_DB_CLIENT_SECRET",
        "ASTRA_DB_KEYSPACE"
    ]
    
    # Optional environment variables
    optional_vars = [
        "ASTRA_DB_SECURE_BUNDLE_PATH",
        "ENVIRONMENT"
    ]
    
    # Check required variables
    missing_vars = []
    for var in required_vars:
        if var in os.environ:
            print(f"✓ Environment variable set: {var}")
        else:
            missing_vars.append(var)
            print(f"✗ Missing environment variable: {var}")
    
    # Check optional variables
    for var in optional_vars:
        if var in os.environ:
            print(f"✓ Optional environment variable set: {var}")
        else:
            print(f"ℹ Optional environment variable not set: {var}")
    
    # Print instructions for missing variables
    if missing_vars:
        print("\nSome required environment variables are missing.")
        print("Create a .env file in the project root with the following variables:")
        for var in missing_vars:
            print(f"{var}=your_{var.lower()}")

def main():
    """Run the setup script."""
    print_header("Aviation Compliance AI Setup")
    
    create_directories()
    create_config_files()
    check_dependencies()
    check_environment_variables()
    
    print_header("Setup Complete")
    print("You can now start using the Aviation Compliance AI system.")
    print("\nNext steps:")
    print("1. Add your regulatory documents to data/raw/faa and data/raw/easa")
    print("2. Process documents with: python scripts/data/process_documents.py")
    print("3. Generate embeddings with: python scripts/data/generate_embeddings.py")
    print("4. Start the application with: python src/app.py")

if __name__ == "__main__":
    main()
```

## Next Steps

After setting up this repository structure, we should focus on implementing the core functionality in this order:

1. **Document Processing Pipeline**: Implement the document readers and processors to handle your existing DOCX files.

2. **Embedding Generation**: Create the embedding generation components to convert processed documents into vector representations.

3. **Vector Storage**: Implement the storage adapters to save and retrieve embeddings.

4. **Retrieval Mechanism**: Develop the retrieval engine to find relevant information based on queries.

5. **Response Generation**: Create the response generation components to provide answers based on retrieved information.

Let me know when you've set up the repository structure, and we can start implementing the document processing pipeline to handle your existing DOCX documents.
