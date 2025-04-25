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
