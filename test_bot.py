#!/usr/bin/env python
"""
GLWIS Academic Bot - Test Suite
Tests bot functionality before deployment
"""

import os
import sys
import openai
import pandas as pd
from io import StringIO

def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*60}")
    print(f"🧪 {text}")
    print(f"{'='*60}")

def test_api_key():
    """Test if API key is configured"""
    print_header("Testing API Key")
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ API Key not found in environment variables")
        return False
    
    if not api_key.startswith("sk-"):
        print("❌ Invalid API key format (should start with sk-)")
        return False
    
    openai.api_key = api_key
    print(f"✅ API Key configured: {api_key[:20]}...")
    return True

def test_dependencies():
    """Test if all dependencies are installed"""
    print_header("Testing Dependencies")
    
    required = {
        'openai': 'OpenAI API',
        'pandas': 'Data Processing',
        'io': 'String IO',
    }
    
    all_ok = True
    for package, description in required.items():
        try:
            __import__(package)
            print(f"✅ {package:<15} - {description}")
        except ImportError:
            print(f"❌ {package:<15} - {description} (NOT INSTALLED)")
            all_ok = False
    
    return all_ok

def test_faq_loading():
    """Test if FAQ data loads correctly"""
    print_header("Testing FAQ Data Loading")
    
    csv_content = """Questions,Answers
What is GLWIS?,"Glorious Living Word International School (GLWIS)"
Where is GLWIS located?,GLWIS is located in Beposo in the Ashanti Region."""
    
    try:
        df = pd.read_csv(StringIO(csv_content))
        print(f"✅ FAQ data loaded successfully")
        print(f"✅ Found {len(df)} FAQ entries")
        print(f"\nSample entries:")
        for idx, row in df.iterrows():
            print(f"   Q: {row['Questions']}")
            print(f"   A: {row['Answers'][:50]}...")
        return True
    except Exception as e:
        print(f"❌ Error loading FAQ data: {e}")
        return False

def test_openai_connection():
    """Test connection to OpenAI API"""
    print_header("Testing OpenAI Connection")
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Skipping (API Key not configured)")
        return None
    
    try:
        # Use a very small request to test connection
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Connection successful' in one sentence."}
            ],
            max_tokens=10,
            temperature=0
        )
        
        if response and response['choices']:
            print(f"✅ OpenAI API connection successful")
            print(f"✅ Response: {response['choices'][0]['message']['content']}")
            return True
        else:
            print("❌ Unexpected API response format")
            return False
            
    except openai.error.AuthenticationError:
        print("❌ Authentication failed - invalid API key")
        return False
    except openai.error.RateLimitError:
        print("⚠️  Rate limit exceeded - try again later")
        return None
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def test_bot_import():
    """Test if bot can be imported"""
    print_header("Testing Bot Import")
    
    try:
        # Check if glwis_bot.py exists
        if not os.path.exists('glwis_bot.py'):
            print("❌ glwis_bot.py not found")
            return False
        
        print("✅ glwis_bot.py found")
        
        # Try to import the bot
        try:
            from glwis_bot import GLWISAcademicBot
            print("✅ Bot class imported successfully")
            
            # Try to instantiate
            bot = GLWISAcademicBot()
            print("✅ Bot instantiated successfully")
            
            if bot.faq_context:
                print(f"✅ FAQ context loaded ({len(bot.faq_context)} characters)")
            
            return True
        except Exception as e:
            print(f"❌ Error importing bot: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_bot_response():
    """Test if bot can generate a response"""
    print_header("Testing Bot Response")
    
    try:
        from glwis_bot import GLWISAcademicBot
        
        bot = GLWISAcademicBot()
        
        # Test with a sample question
        test_question = "Where is GLWIS located?"
        print(f"Test Question: {test_question}")
        
        response = bot.answer_question(test_question)
        
        if response:
            print(f"✅ Bot response received")
            print(f"\nResponse Preview:")
            print(f"{response[:200]}...")
            return True
        else:
            print("❌ No response from bot")
            return False
            
    except Exception as e:
        print(f"❌ Error testing bot response: {e}")
        return False

def run_all_tests():
    """Run all tests and summarize"""
    print("\n" + "🎓"*30)
    print("GLWIS ACADEMIC BOT - TEST SUITE")
    print("🎓"*30)
    
    tests = [
        ("Dependencies", test_dependencies),
        ("API Key", test_api_key),
        ("FAQ Loading", test_faq_loading),
        ("OpenAI Connection", test_openai_connection),
        ("Bot Import", test_bot_import),
        ("Bot Response", test_bot_response),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            result = test_func()
            results[test_name] = result
        except Exception as e:
            print(f"❌ Unexpected error in {test_name}: {e}")
            results[test_name] = False
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)
    
    print(f"\n📊 Results:")
    print(f"   ✅ Passed:  {passed}")
    print(f"   ❌ Failed:  {failed}")
    print(f"   ⏭️  Skipped: {skipped}")
    
    print(f"\n📋 Test Details:")
    for test_name, result in results.items():
        status = "✅" if result is True else "❌" if result is False else "⏭️"
        print(f"   {status} {test_name}")
    
    print("\n" + "="*60)
    
    if failed == 0:
        print("✅ ALL TESTS PASSED - Bot is ready to use!")
        print("\nStart the bot with: python glwis_bot.py")
    else:
        print(f"❌ {failed} test(s) failed - Fix issues before using bot")
        print("\nCheck the details above and troubleshoot accordingly.")
    
    print("="*60 + "\n")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
