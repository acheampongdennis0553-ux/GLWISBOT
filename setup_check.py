#!/usr/bin/env python
"""
GLWIS Academic Bot - Quick Start Guide
Run this script to get started with the bot
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key.startswith("sk-"):
        print(f"✅ OpenAI API key found: {api_key[:10]}...")
        return True
    else:
        print("⚠️  OpenAI API key not found")
        print("   Set OPENAI_API_KEY environment variable or add to .env file")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required = ['openai', 'pandas']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            missing.append(package)
    
    if missing:
        print(f"\n📦 Install missing packages with:")
        print(f"   pip install {' '.join(missing)}")
        return False
    return True

def check_files():
    """Check if necessary files exist"""
    required_files = ['glwis_bot.py', 'requirements.txt']
    all_exist = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} found")
        else:
            print(f"❌ {file} NOT found")
            all_exist = False
    
    return all_exist

def create_env_file():
    """Help user create .env file"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    print("\n📝 Creating .env file...")
    api_key = input("Enter your OpenAI API key (starts with sk-): ").strip()
    
    if api_key.startswith("sk-"):
        with open('.env', 'w') as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        print("✅ .env file created successfully")
        return True
    else:
        print("❌ Invalid API key format")
        return False

def main():
    """Run setup checks"""
    print("=" * 60)
    print("🎓 GLWIS Academic Bot - Setup Check")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Project Files", check_files),
        ("OpenAI API Key", check_api_key),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n🔍 Checking {name}...")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("✅ All checks passed!")
        print("\n🚀 To start the bot, run:")
        print("   python glwis_bot.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        
        if not os.path.exists('.env'):
            create_env = input("\nWould you like to create a .env file? (y/n): ").strip().lower()
            if create_env == 'y':
                create_env_file()
    
    print()

if __name__ == "__main__":
    main()
