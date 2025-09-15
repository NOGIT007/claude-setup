# Deployment Commands

## Description
Deployment commands for Google Cloud Run and other platforms.

## Google Cloud Run Deployment

### Pre-flight Checks
```bash
# Check environment variables
cat .env | grep -E "GCP_REGION|GCP_PROJECT"

# Verify dependencies
uv lock --upgrade
uv sync

# Test Docker build
docker build -f Dockerfile -t test-app .
docker run -p 8080:8080 test-app
```

### Deploy to Cloud Run
```bash
# Deploy with authentication (REQUIRED)
gcloud run deploy my-service \
  --source . \
  --platform managed \
  --region ${GCP_REGION} \
  --no-allow-unauthenticated

# Monitor deployment
gcloud run services list --region ${GCP_REGION}
```

### Post-deployment Verification
```bash
# Create authenticated proxy
gcloud run services proxy my-service --region ${GCP_REGION}

# Check logs
gcloud run services logs read my-service --region ${GCP_REGION} --limit=50

# Test endpoints
curl http://127.0.0.1:8080/health
```

### FastMCP Deployment
```bash
# For MCP servers on Cloud Run
gcloud run deploy mcp-server \
  --source . \
  --platform managed \
  --region ${GCP_REGION} \
  --no-allow-unauthenticated \
  --port 8080
```

## Security Checklist
- [ ] Never skip `--no-allow-unauthenticated`
- [ ] Use Secret Manager for API keys
- [ ] Set up IAM roles properly
- [ ] Monitor access logs

## Token Usage
Estimated: ~0.3k tokens

## Usage
Add this line to your CLAUDE.md for deployment support:
```
## Active Commands
- deployment: Cloud Run deployment commands and checklist
```