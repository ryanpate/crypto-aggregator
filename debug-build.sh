#!/bin/bash
echo "=== Hugo Version ==="
hugo version

echo -e "\n=== Directory Structure ==="
find . -type d -name "node_modules" -prune -o -type d -name ".git" -prune -o -type d -print | head -20

echo -e "\n=== Content Files ==="
find content -name "*.md" | head -10

echo -e "\n=== Layout Files ==="
find layouts -name "*.html" | head -20

echo -e "\n=== Config File ==="
head -20 config.toml

echo -e "\n=== Building Site ==="
hugo --verbose

echo -e "\n=== Build Complete ==="