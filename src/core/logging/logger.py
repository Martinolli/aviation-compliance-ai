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
        logging.getLogger("httpx") .setLevel(logging.WARNING)
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
