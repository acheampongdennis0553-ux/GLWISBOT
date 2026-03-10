"""
GLWIS Academic Bot - Web Interface Quick Start
Run this to start the bot with web interface
"""

import subprocess
import sys
import os
import time
import webbrowser

def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    print(f"✅ Python {sys.version.split()[0]}")
    return True

def check_flask_installed():
    """Check if Flask is installed"""
    try:
        import flask
        print(f"✅ Flask {flask.__version__} installed")
        return True
    except ImportError:
        print("❌ Flask not installed")
        return False

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key.startswith("sk-"):
        print(f"✅ API key configured: {api_key[:15]}...")
        return True
    print("❌ API key not found")
    return False

def main():
    print("\n" + "="*60)
    print("🎓 GLWIS ACADEMIC BOT - WEB INTERFACE")
    print("="*60)
    
    print("\n🔍 Checking requirements...")
    
    checks = [
        ("Python Version", check_python_version),
        ("Flask Installation", check_flask_installed),
        ("API Key", check_api_key),
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n  {name}:")
        if not check_func():
            all_passed = False
    
    if not all_passed:
        print("\n" + "="*60)
        print("⚠️  Some checks failed!")
        print("\nQuick fixes:")
        print("  1. Install Flask: pip install Flask")
        print("  2. Create .env file with: OPENAI_API_KEY=sk-your-key")
        print("="*60 + "\n")
        return
    
    print("\n" + "="*60)
    print("✅ All checks passed!")
    print("="*60)
    
    print("\n🚀 Starting web server...")
    print("   Opening http://localhost:5000 in your browser...\n")
    
    try:
        # Give the server a moment to start before opening browser
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
    except:
        pass
    
    print("\nℹ️  Access the bot at: http://localhost:5000")
    print("   Press Ctrl+C to stop the server\n")
    
    # Start Flask app
    try:
        os.system('python app.py')
    except KeyboardInterrupt:
        print("\n\n✅ Web server stopped. Goodbye!")

if __name__ == "__main__":
    main()
