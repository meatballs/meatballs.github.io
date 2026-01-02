# Batch ID Creation for Swarm Deployment

## Prerequisites

- Bee node running and accessible
- swarm-cli installed and configured
- Sufficient funds in your Bee node

## Creating a New Batch ID

1. **Create the batch directly:**
   ```bash
   swarm-cli postage stamp create --depth 20 --amount 0.1
   ```

2. **Get the batch ID:**
   ```bash
   swarm-cli postage stamps
   ```
   Look for the batch ID in the output (starts with 0x...)

3. **Add to .env file:**
   ```bash
   cp .env.example .env
   # Edit .env and add your batch ID as SWARM_BATCH_ID
   ```

## Batch Configuration

- **Depth 20**: Suitable for personal website
- **Amount 0.1**: 0.1 xBZZ (adjust based on content size and duration)
- **Duration**: Typically lasts several months depending on usage

## Verification

After creating batch:
```bash
just status
# Should show your new batch details (once SWARM_BATCH_ID is set in .env)
```

## Initial Deployment

Once batch ID is configured:
```bash
just deploy-all
```

This will:
1. Build the site
2. Upload to Swarm
3. Generate SWARM_FEED_MANIFEST
4. Verify deployment through multiple gateways

## Gateway Access

After successful deployment, your site will be available at:
- https://owencampbell.eth.limo
- https://owencampbell.eth.link  
- https://owencampbell.bzz.link