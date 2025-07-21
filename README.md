# Multi-Modal Storyboard and Video Scene Generator

A comprehensive creative pipeline that transforms simple story ideas into visual storyboards and short video scenes using AI-powered tools.

## Overview

This project implements an end-to-end creative workflow that takes a high-level text prompt and generates:
1. **Detailed Script**: Using Large Language Models for scene descriptions and character actions
2. **Visual Storyboard**: Text-to-image generation for key scenes
3. **Video Scenes**: Short 3-5 second video clips from storyboard images

## Features

- **Intelligent Scripting**: Converts simple prompts into detailed, structured scripts
- **Visual Storyboarding**: Generates compelling images for each scene
- **Video Generation**: Creates short video clips from storyboard frames
- **Modular Architecture**: Easy to extend and modify individual components
- **Professional Output**: Publication-ready storyboards and videos

## Project Structure

```
storyboard-generator/
├── src/
│   ├── script_generator.py      # LLM-based script generation
│   ├── storyboard_generator.py  # Text-to-image generation
│   ├── video_generator.py       # Image-to-video generation
│   └── pipeline.py              # Main orchestration
├── config/
│   └── settings.py              # Configuration and API keys
├── output/
│   ├── scripts/                 # Generated scripts
│   ├── storyboards/             # Generated images
│   └── videos/                  # Generated video clips
├── requirements.txt
└── main.py                      # Entry point
```

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure API keys in `config/settings.py`
4. Run: `python main.py "your story prompt here"`

## Example Usage

```bash
python main.py "a detective discovering a clue in a rainy city at night"
```

This will generate:
- A detailed script with scene breakdowns
- Storyboard images for each key scene
- Short video clips bringing scenes to life

## Technology Stack

- **Python 3.8+**: Core development language
- **OpenAI GPT**: Script generation and scene descriptions
- **Stability AI**: Image generation for storyboards
- **Stable Video Diffusion**: Video generation from images
- **PIL/OpenCV**: Image and video processing

## Author

Created as part of an internship project demonstrating AI-powered creative workflows and multi-modal content generation.