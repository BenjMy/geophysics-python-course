#!/usr/bin/env python3
"""
Download sample datasets for the course
"""
import os
from pathlib import Path


def create_sample_data():
    """Create placeholder sample data files"""
    print("📊 Creating sample data files...")
    
    # Create sample resistivity data
    resistivity_path = Path("data/sample_resistivity")
    resistivity_path.mkdir(parents=True, exist_ok=True)
    
    # Create sample EM data
    em_path = Path("data/sample_em")
    em_path.mkdir(parents=True, exist_ok=True)
    
    print("✅ Sample data structure created!")
    print("Note: Add actual data files to these directories")


if __name__ == "__main__":
    create_sample_data()
