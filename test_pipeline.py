#!/usr/bin/env python3
"""
Test script for the Multi-Modal Storyboard Generator
Run this to test individual components
"""
import os
import sys
from config.settings import Config

def test_configuration():
    """Test if configuration is properly set up"""
    print("🔧 Testing Configuration...")
    
    try:
        Config.validate_keys()
        print("✅ API keys are configured")
        return True
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_script_generation():
    """Test script generation only"""
    print("\n📝 Testing Script Generation...")
    
    try:
        from src.script_generator import ScriptGenerator
        
        generator = ScriptGenerator()
        script_data = generator.generate_script("a simple test story about a cat finding a treasure")
        
        print(f"✅ Script generated: {script_data['title']}")
        print(f"   Scenes: {len(script_data['scenes'])}")
        return True
        
    except Exception as e:
        print(f"❌ Script generation failed: {e}")
        return False

def test_imports():
    """Test if all required modules can be imported"""
    print("\n📦 Testing Imports...")
    
    modules_to_test = [
        ('openai', 'OpenAI'),
        ('PIL', 'Pillow'),
        ('cv2', 'OpenCV'),
        ('torch', 'PyTorch'),
        ('requests', 'Requests'),
    ]
    
    all_good = True
    
    for module_name, display_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {display_name} imported successfully")
        except ImportError as e:
            print(f"❌ {display_name} import failed: {e}")
            all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("🧪 Multi-Modal Storyboard Generator - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_configuration),
        ("Script Generation Test", test_script_generation),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(results)} tests")
    
    if passed == len(results):
        print("\n🎉 All tests passed! You're ready to generate storyboards.")
    else:
        print("\n⚠️  Some tests failed. Please check the setup instructions.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())