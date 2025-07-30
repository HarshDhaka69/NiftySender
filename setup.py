#!/usr/bin/env python3
"""
NiftyPool Setup Script
"""

import os
import sys
import subprocess
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating project directories...")
    directories = ["data", "logs", "sessions", "backups"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def setup_project():
    """Main setup function"""
    print("🚀 NiftyPool Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        return False
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Get your Telegram API credentials from https://my.telegram.org/apps")
    print("2. Run: python main.py")
    print("3. Follow the setup wizard to add your account")
    print("\n📞 Contact @ItsHarshX for support")
    
    return True

if __name__ == "__main__":
    try:
        success = setup_project()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1) 