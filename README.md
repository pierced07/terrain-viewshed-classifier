# Terrain Viewshed & Classifier
**Real-time geospatial perception pipeline for autonomous systems**

## Anduril Relevance
This project directly supports Frontier Systems' mission to "build terrain rendering systems used in live operations (viewsheds, classifications)." It demonstrates:
- **Line-of-sight computation** for operator situational awareness
- **Slope-based terrain classification** for autonomous routing
- **Hybrid C++/Python architecture** suitable for edge deployment on embedded systems

## Quick Start

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt

mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j4
cd ..

python main.py