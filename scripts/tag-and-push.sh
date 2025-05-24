#!/usr/bin/env bash
# Tag and push the current version from pyproject.toml

set -e

PYPROJECT="hungovercoders-repo-tools/pyproject.toml"
VERSION=$(grep '^version' "$PYPROJECT" | head -1 | cut -d '"' -f2)
TAG="v$VERSION"

echo "Detected version: $VERSION"

git tag "$TAG"
git push origin "$TAG"
echo "Tag $TAG created and pushed."
