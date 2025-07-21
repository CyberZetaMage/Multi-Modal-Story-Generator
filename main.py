#!/usr/bin/env python3
"""
Multi-Modal Storyboard and Video Scene Generator
Main entry point for the application

Usage:
    python main.py "your story prompt here"
    python main.py --script-only "your story prompt here"
    python main.py --help
"""
import sys
import argparse
from config.settings import Config
from src.pipeline import StoryboardPipeline

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description="Multi-Modal Storyboard and Video Scene Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python main.py "a detective discovering a clue in a rainy city at night"
    python main.py --script-only "a space explorer finding alien artifacts"
    python main.py "a chef preparing a magical meal in an enchanted kitchen"
        """
    )
    
    parser.add_argument(
        'prompt',
        help='Story prompt to generate storyboard from'
    )
    
    parser.add_argument(
        '--script-only',
        action='store_true',
        help='Generate only the script without images or videos'
    )
    
    parser.add_argument(
        '--validate-config',
        action='store_true',
        help='Validate configuration and API keys'
    )
    
    args = parser.parse_args()
    
    # Validate configuration
    try:
        Config.validate_keys()
        print("✅ Configuration validated successfully")
        
        if args.validate_config:
            print("Configuration is valid. You can proceed with generation.")
            return
            
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nPlease set up your API keys:")
        print("1. Create a .env file in the project root")
        print("2. Add your API keys:")
        print("   OPENAI_API_KEY=your_openai_key_here")
        print("   STABILITY_API_KEY=your_stability_key_here")
        print("\nOr set them as environment variables.")
        return 1
    
    # Initialize pipeline
    pipeline = StoryboardPipeline()
    
    # Generate content based on arguments
    if args.script_only:
        print("🎬 Script-only mode selected")
        result = pipeline.generate_script_only(args.prompt)
        
        if result['success']:
            print(f"\n📄 Script saved to: {result['script_path']}")
        else:
            print(f"\n❌ Failed: {result.get('error', 'Unknown error')}")
            return 1
    else:
        print("🎬 Full pipeline mode selected")
        result = pipeline.generate_complete_storyboard(args.prompt)
        
        if not result['success']:
            print(f"\n❌ Pipeline failed: {result.get('error', 'Unknown error')}")
            return 1
    
    print("\n🎉 Generation completed successfully!")
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code or 0)
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)