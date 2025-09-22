#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Get the short git hash for tagging
GIT_HASH=$(git rev-parse --short HEAD)
IMAGE_NAME="personal-research-assistant"
IMAGE_TAG="${IMAGE_NAME}:${GIT_HASH}"

echo "--- 1. Running Linter and Formatter ---"
ruff check . --fix
black .
isort .

echo "--- 2. Running Tests in Clean Container Environment ---"
# Uses the mandatory 'mcp' alias if available, otherwise fallback to local pytest
if command -v docker &> /dev/null && alias mcp &> /dev/null; then
    echo "Using containerized tests with mcp alias"
    mcp pytest
else
    echo "Docker/mcp alias not available, running tests locally"
    pytest
fi

echo "--- 3. Building Docker Image: ${IMAGE_TAG} ---"
docker build -t "${IMAGE_TAG}" .

echo "--- 4. Scanning Image for Vulnerabilities ---"
# Fails the script if critical vulnerabilities are found
# Gracefully skip if trivy not installed
if command -v trivy &> /dev/null; then
    echo "Running Trivy vulnerability scan..."
    trivy image --severity CRITICAL "${IMAGE_TAG}"
else
    echo "⚠️  Trivy not installed, skipping vulnerability scan"
    echo "   Install with: curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin"
fi

echo "--- 5. Pushing Image to Registry (Optional) ---"
# Uncomment and configure for your registry (e.g., Docker Hub, GCP Artifact Registry)
# echo "Tagging for registry..."
# docker tag "${IMAGE_TAG}" "your-registry/${IMAGE_TAG}"
# echo "Pushing to registry..."
# docker push "your-registry/${IMAGE_TAG}"

echo "--- 6. Deploy to Environment (Optional) ---"
# Add your deployment commands here
# Example for Render (using Deploy Hook):
# if [ -n "${RENDER_DEPLOY_HOOK_URL}" ]; then
#     echo "Triggering Render deployment..."
#     curl -X POST "${RENDER_DEPLOY_HOOK_URL}"
# fi

echo "✅ Deployment script finished successfully."
echo "🐳 Built image: ${IMAGE_TAG}"
echo "💡 Next steps:"
echo "   - Push to GitHub to trigger CI/CD"
echo "   - Or manually push image to registry and deploy"