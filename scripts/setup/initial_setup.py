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
