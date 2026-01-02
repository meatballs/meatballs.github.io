# Batch ID Creation for Swarm Deployment

## Prerequisites

- Bee node running and accessible
- swarm-cli installed and configured
- Sufficient funds in your Bee node

## Creating a New Postage Stamp

1. **Create stamp directly:**
   ```bash
   swarm-cli stamp create --capacity 1GB --ttl 6month
   ```

2. **Get the batch ID:**
   ```bash
   swarm-cli stamp list
   ```
   Look for batch ID in the output (starts with 0x...)

3. **Add to .env file:**
   ```bash
   cp .env.example .env
   # Edit .env and add your batch ID as SWARM_BATCH_ID
   ```

## Stamp Configuration

- **Capacity 1GB**: Suitable for personal website with room to grow
- **TTL 6month**: Duration before stamp expires (adjust as needed)
- **Immutable**: Default is true, preventing accidental overwrites

## Alternative Options

**Different capacities/time periods:**
```bash
# Smaller site, shorter duration:
swarm-cli stamp create --capacity 500MB --ttl 3month

# Larger site, longer duration:  
swarm-cli stamp create --capacity 2GB --ttl 12month
```

## Extending Existing Stamp

If your stamp is about to expire:
```bash
swarm-cli stamp extend <batch-id> --ttl 6month
```

## Cost Considerations

- **Capacity-based pricing**: You pay for storage capacity, not bandwidth
- **Time-based TTL**: Longer duration costs proportionally more
- **1GB for 6 months**: Typical cost range for personal websites
- **Immutable stamps**: Generally cheaper than mutable ones
- **Extension**: You can extend existing stamps without purchasing new ones

**Tip**: Start with smaller capacity/shorter duration for testing, then create larger stamp once comfortable with the process.

## Verification

After creating batch:
```bash
swarm-cli stamp list
# Should show your new stamp in the list
```

Once SWARM_BATCH_ID is set in .env:
```bash
just status
# Should show your batch stamp details
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