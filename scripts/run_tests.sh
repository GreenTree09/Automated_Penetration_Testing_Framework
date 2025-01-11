#!/bin/bash

# Run C++ tests
cd build
ctest

# Run Python tests
cd ..
pytest tests/

echo "All tests executed."