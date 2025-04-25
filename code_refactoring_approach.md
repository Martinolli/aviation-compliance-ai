# Code Structure Refactoring Approach

## Overview
This document outlines a systematic approach to refactoring the Aviation Compliance AI codebase, transforming it from its current mixed Python/JavaScript implementation with overlapping functionality into a modular, maintainable, and extensible architecture. The refactoring will be implemented incrementally to ensure continuous functionality while improving the system.

## Current Architecture Assessment

### Strengths
- Functional RAG pipeline implementation
- Working document processing capabilities
- Effective embedding generation and storage
- Functional retrieval mechanism
- Basic visualization capabilities

### Limitations
- Mixed Python and JavaScript with duplicated functionality
- Hardcoded paths and configuration
- Inconsistent error handling
- Limited modularity and separation of concerns
- Lack of standardized interfaces between components
- Minimal testing infrastructure

## Target Architecture

### Directory Structure
```
/aviation-compliance-ai/
├── src/
│   ├── core/                  # Core RAG functionality
│   │   ├── config.py          # Centralized configuration
│   │   ├── logging.py         # Logging configuration
│   │   └── exceptions.py      # Custom exception classes
│   ├── data/                  # Data processing
│   │   ├── readers/           # Document readers for different formats
│   │   ├── processors/        # Text processing and cleaning
│   │   ├── chunkers/          # Document chunking strategies
│   │   └── extractors/        # Metadata and entity extraction
│   ├── embeddings/            # Embedding generation and management
│   │   ├── models/            # Embedding model interfaces
│   │   ├── generators/        # Embedding generation logic
│   │   └── optimizers/        # Embedding optimization utilities
│   ├── storage/               # Data storage interfaces
│   │   ├── vector_db/         # Vector database adapters
│   │   ├── document_store/    # Document storage adapters
│   │   └── cache/             # Caching mechanisms
│   ├── retrieval/             # Retrieval mechanisms
│   │   ├── engines/           # Search engine implementations
│   │   ├── rankers/           # Result ranking algorithms
│   │   └── filters/           # Query and result filters
│   ├── generation/            # Response generation
│   │   ├── prompts/           # Prompt templates and management
│   │   ├── validators/        # Response validation
│   │   └── formatters/        # Response formatting
│   ├── knowledge/             # Domain-specific knowledge
│   │   ├── regulatory/        # Regulatory framework models
│   │   ├── safety/            # Safety analysis frameworks
│   │   └── aviation/          # Aviation-specific knowledge
│   ├── api/                   # API interfaces
│   │   ├── rest/              # REST API implementation
│   │   └── websocket/         # WebSocket implementation for real-time features
│   └── ui/                    # User interface components
│       ├── web/               # Web interface
│       └── cli/               # Command-line interface
├── scripts/                   # Standalone utility scripts
├── tests/                     # Test suite
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test fixtures
├── docs/                      # Documentation
├── config/                    # Configuration files
└── data/                      # Data directory
    ├── raw/                   # Raw document storage
    ├── processed/             # Processed documents
    ├── embeddings/            # Generated embeddings
    └── regulatory/            # Regulatory document storage
```

### Component Interfaces

#### 1. Document Processing Interface
```python
class DocumentProcessor:
    """Interface for document processing components."""
    
    def process(self, document_path: str) -> ProcessedDocument:
        """Process a document and return a processed representation."""
        pass
        
class ProcessedDocument:
    """Representation of a processed document."""
    
    def __init__(self, text: str, metadata: dict, chunks: List[DocumentChunk]):
        self.text = text
        self.metadata = metadata
        self.chunks = chunks
```

#### 2. Embedding Generation Interface
```python
class EmbeddingGenerator:
    """Interface for embedding generation components."""
    
    def generate(self, text: str) -> List[float]:
        """Generate an embedding for the given text."""
        pass
        
    def generate_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        pass
```

#### 3. Vector Database Interface
```python
class VectorDatabase:
    """Interface for vector database operations."""
    
    def store(self, id: str, embedding: List[float], metadata: dict) -> bool:
        """Store an embedding with metadata."""
        pass
        
    def search(self, query_embedding: List[float], k: int = 10) -> List[SearchResult]:
        """Search for similar embeddings."""
        pass
        
    def delete(self, id: str) -> bool:
        """Delete an embedding by ID."""
        pass
```

#### 4. Retrieval Interface
```python
class Retriever:
    """Interface for retrieval components."""
    
    def retrieve(self, query: str, k: int = 10) -> List[RetrievalResult]:
        """Retrieve relevant documents for a query."""
        pass
```

#### 5. Generation Interface
```python
class Generator:
    """Interface for response generation components."""
    
    def generate(self, query: str, context: List[str]) -> GenerationResult:
        """Generate a response for a query with context."""
        pass
```

## Refactoring Strategy

### Phase 1: Foundation Setup (Week 1)

#### 1. Project Structure Creation
- Create the new directory structure
- Set up version control with branching strategy
- Implement basic CI/CD pipeline

#### 2. Core Module Implementation
- Create configuration management module
- Implement logging framework
- Define custom exception classes
- Develop utility functions

#### 3. Interface Definition
- Define interfaces for all major components
- Create abstract base classes
- Document interface contracts

### Phase 2: Component Migration (Weeks 2-3)

#### 1. Document Processing Migration
- Refactor document reading functionality
  - Extract from `read_documents.py` to `src/data/readers/`
  - Create format-specific readers (PDF, DOCX)
  - Implement common interface

- Refactor text processing
  - Extract from `read_documents.py` to `src/data/processors/`
  - Create specialized processors for cleaning, normalization
  - Implement aviation-specific text processing

- Refactor chunking logic
  - Create semantic chunking implementation
  - Implement chunk metadata enhancement
  - Add regulatory structure awareness

#### 2. Embedding Generation Migration
- Refactor embedding generation
  - Extract from `generate_embeddings.js` to `src/embeddings/generators/`
  - Create Python implementation with same functionality
  - Add support for multiple embedding models

- Implement embedding optimization
  - Create caching mechanism
  - Add incremental update support
  - Implement batch processing

#### 3. Storage Migration
- Refactor vector database operations
  - Extract from `store_embeddings_astra.js` to `src/storage/vector_db/`
  - Create AstraDB adapter implementation
  - Add support for alternative vector databases

- Implement document storage
  - Create document storage interface
  - Implement file system adapter
  - Add support for metadata indexing

### Phase 3: Pipeline Integration (Week 4)

#### 1. Retrieval Migration
- Refactor retrieval mechanism
  - Extract from `aviationai.py` to `src/retrieval/engines/`
  - Implement hybrid search capabilities
  - Add result ranking and filtering

#### 2. Generation Migration
- Refactor response generation
  - Extract from `aviationai.py` to `src/generation/`
  - Implement prompt template management
  - Add response validation and formatting

#### 3. Pipeline Manager Refactoring
- Refactor pipeline manager
  - Extract from `aviationrag_manager.py` to core module
  - Implement modular pipeline configuration
  - Add pipeline monitoring and logging

### Phase 4: Testing and Documentation (Week 5)

#### 1. Test Suite Implementation
- Create unit tests for all components
- Implement integration tests for the pipeline
- Add performance benchmarks

#### 2. Documentation
- Create API documentation
- Write developer guide
- Create architecture diagrams

#### 3. Migration Validation
- Verify functionality matches original system
- Benchmark performance against original system
- Address any regressions or issues

## Migration Approach for Specific Files

### 1. aviationai.py

#### Current Functionality
- OpenAI client initialization
- Embedding generation
- Document retrieval
- Response generation
- Chat loop management

#### Migration Plan
1. Extract configuration to `src/core/config.py`
2. Move embedding generation to `src/embeddings/generators/openai_generator.py`
3. Refactor retrieval to `src/retrieval/engines/faiss_retriever.py`
4. Move response generation to `src/generation/generators/openai_generator.py`
5. Refactor chat loop to `src/ui/cli/chat_interface.py`
6. Create integration in `src/core/pipeline.py`

### 2. read_documents.py

#### Current Functionality
- Document reading from PDF and DOCX
- Text preprocessing
- Entity extraction
- Document classification

#### Migration Plan
1. Create format-specific readers:
   - `src/data/readers/pdf_reader.py`
   - `src/data/readers/docx_reader.py`
2. Implement text processors:
   - `src/data/processors/text_cleaner.py`
   - `src/data/processors/text_normalizer.py`
3. Create entity extractors:
   - `src/data/extractors/entity_extractor.py`
   - `src/data/extractors/metadata_extractor.py`
4. Implement document classifier in `src/data/processors/document_classifier.py`

### 3. generate_embeddings.js

#### Current Functionality
- OpenAI embedding generation
- Batch processing
- Checkpoint saving
- CSV report generation

#### Migration Plan
1. Create Python implementation in `src/embeddings/generators/openai_generator.py`
2. Implement batch processing in `src/embeddings/batch_processor.py`
3. Add checkpoint management in `src/core/checkpoint_manager.py`
4. Move reporting to `src/core/reporting.py`

### 4. store_embeddings_astra.js

#### Current Functionality
- AstraDB connection
- Embedding storage
- Duplicate checking

#### Migration Plan
1. Create AstraDB adapter in `src/storage/vector_db/astra_adapter.py`
2. Implement embedding storage manager in `src/storage/embedding_storage.py`
3. Add duplicate detection in `src/storage/duplicate_detector.py`

### 5. aviationrag_manager.py

#### Current Functionality
- Pipeline orchestration
- Script execution
- Logging and reporting

#### Migration Plan
1. Create pipeline manager in `src/core/pipeline_manager.py`
2. Implement task scheduler in `src/core/task_scheduler.py`
3. Add execution tracker in `src/core/execution_tracker.py`
4. Create reporting module in `src/core/reporting.py`

## Dependency Management

### Python Dependencies
Create `requirements.txt` with:
```
openai>=1.0.0
numpy>=1.20.0
pandas>=1.3.0
faiss-cpu>=1.7.0
pdfplumber>=0.7.0
python-docx>=0.8.11
spacy>=3.2.0
nltk>=3.6.0
tiktoken>=0.3.0
tqdm>=4.62.0
python-dotenv>=0.19.0
fastapi>=0.68.0
uvicorn>=0.15.0
pytest>=6.2.5
```

### JavaScript Dependencies
Create `package.json` with:
```json
{
  "dependencies": {
    "openai": "^4.0.0",
    "cassandra-driver": "^4.6.0",
    "dotenv": "^10.0.0",
    "csv-writer": "^1.6.0"
  },
  "devDependencies": {
    "jest": "^27.0.0"
  }
}
```

## Configuration Management

### Environment Variables
Create `.env.example` with:
```
# OpenAI Configuration
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

### Configuration File
Create `config/default.yaml` with:
```yaml
application:
  name: Aviation Compliance AI
  version: 1.0.0

paths:
  data: ./data
  raw: ${paths.data}/raw
  processed: ${paths.data}/processed
  embeddings: ${paths.data}/embeddings
  regulatory: ${paths.data}/regulatory
  logs: ./logs

embedding:
  model: text-embedding-ada-002
  dimensions: 1536
  batch_size: 10
  max_retries: 3
  retry_delay: 1000

retrieval:
  k: 20
  max_tokens: 6000
  min_similarity: 0.7

generation:
  model: gpt-4-turbo
  temperature: 0.6
  max_tokens: 2000
```

## Error Handling Strategy

### Custom Exception Hierarchy
```python
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
```

### Error Handling Pattern
```python
def process_with_retries(func, *args, max_retries=3, **kwargs):
    """Execute a function with retry logic."""
    last_exception = None
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt+1}/{max_retries} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    
    logger.error(f"All {max_retries} attempts failed")
    raise last_exception
```

## Logging Strategy

### Logging Configuration
```python
import logging
import os
from datetime import datetime

def setup_logging(log_dir, log_level=logging.INFO):
    """Set up logging with file and console handlers."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"aviation_compliance_{timestamp}.log")
    
    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Suppress verbose logging from libraries
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    
    return root_logger
```

## Testing Strategy

### Unit Testing
```python
# Example unit test for document processor
import pytest
from src.data.processors.text_cleaner import TextCleaner

def test_text_cleaner_removes_special_characters():
    cleaner = TextCleaner()
    text = "This is a test with special characters: @#$%^&*"
    cleaned_text = cleaner.clean(text)
    assert "@#$%^&*" not in cleaned_text
    assert "This is a test with special characters" in cleaned_text
```

### Integration Testing
```python
# Example integration test for document processing pipeline
import pytest
from src.data.pipeline import DocumentProcessingPipeline
from src.data.readers.pdf_reader import PDFReader
from src.data.processors.text_cleaner import TextCleaner
from src.data.chunkers.semantic_chunker import SemanticChunker

def test_document_processing_pipeline():
    # Create pipeline components
    reader = PDFReader()
    cleaner = TextCleaner()
    chunker = SemanticChunker(chunk_size=1000, overlap=200)
    
    # Create pipeline
    pipeline = DocumentProcessingPipeline(
        reader=reader,
        processors=[cleaner],
        chunker=chunker
    )
    
    # Process test document
    result = pipeline.process("tests/fixtures/test_document.pdf")
    
    # Verify results
    assert result is not None
    assert len(result.chunks) > 0
    assert all(len(chunk.text) > 0 for chunk in result.chunks)
```

## Implementation Timeline

### Week 1: Foundation Setup
- Day 1-2: Create project structure and core modules
- Day 3-4: Define interfaces and abstract classes
- Day 5: Set up CI/CD pipeline and testing framework

### Week 2: Document Processing Migration
- Day 1-2: Implement document readers
- Day 3-4: Create text processors
- Day 5: Develop chunking strategies

### Week 3: Embedding and Storage Migration
- Day 1-2: Implement embedding generators
- Day 3-4: Create storage adapters
- Day 5: Develop caching and optimization

### Week 4: Pipeline Integration
- Day 1-2: Implement retrieval components
- Day 3-4: Create generation components
- Day 5: Develop pipeline manager

### Week 5: Testing and Documentation
- Day 1-2: Write unit and integration tests
- Day 3-4: Create documentation
- Day 5: Validate migration and fix issues

## Conclusion

This refactoring approach provides a systematic path to transform the Aviation Compliance AI codebase into a modular, maintainable, and extensible architecture. By following this incremental approach, the system can be improved while maintaining functionality throughout the refactoring process.

The new architecture will provide several benefits:
1. Clear separation of concerns with well-defined interfaces
2. Improved maintainability through modular design
3. Enhanced extensibility for adding new features
4. Better error handling and logging
5. Comprehensive testing framework
6. Consistent configuration management

This refactoring will set a solid foundation for implementing the regulatory integration and accident analysis capabilities outlined in the implementation plan.
