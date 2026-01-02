# Swarm deployment commands for Owen Campbell website
# Environment variables stored in .env file (never committed)

# Load environment variables from .env file
set dotenv-load := true

# Build website
build:
    hugo

# Deploy to Swarm (build + upload, no verification)
deploy: build
    swarm-cli feed upload ./public \
      --identity owencampbell-website \
      --topic-string "owencampbell-website-main" \
      --stamp $SWARM_BATCH_ID \
      --index-document index.html \
      --error-document 404.html \
      --pin

# Verify deployment (check uploaded content)
verify:
    swarm-cli feed print --identity owencampbell-website --topic-string "owencampbell-website-main"
    echo ""
    echo "Testing gateway access..."
    curl -s -I https://owencampbell.eth.limo | head -5

# Check Swarm status
status:
    swarm-cli status
    echo ""
    echo "Stamp status:"
    swarm-cli stamp show $SWARM_BATCH_ID

# Show current configuration
show-config:
    echo "Batch ID: $SWARM_BATCH_ID"
    echo "Feed Manifest: $SWARM_FEED_MANIFEST"

# Full deployment workflow (build + deploy + verify)
deploy-all: build deploy verify

