# 🚀 Render Deployment Guide - Personal Research Assistant

This guide provides step-by-step instructions for deploying your Personal Research Assistant to Render.com with a public GitHub repository.

## 📋 Prerequisites

Before starting, ensure you have:
- ✅ Your code pushed to a **public GitHub repository**
- ✅ All required API keys ready (see API Keys section below)
- ✅ A Render.com account (free tier is sufficient)

---

## 🔑 Step 1: Obtain Required API Keys

### 1.1 OpenRouter API Key
1. Go to [https://openrouter.ai/](https://openrouter.ai/)
2. Click **"Sign Up"** or **"Log In"**
3. Navigate to **"API Keys"** section
4. Click **"Create API Key"**
5. Copy the generated key (starts with `sk-or-v1-...`)
6. **Save this key** - you'll need it in Step 3

### 1.2 Groq API Key
1. Go to [https://console.groq.com/](https://console.groq.com/)
2. Sign up with your email or Google account
3. Navigate to **"API Keys"** in the left sidebar
4. Click **"Create API Key"**
5. Give it a name (e.g., "Personal Research Assistant")
6. Copy the generated key (starts with `gsk_...`)
7. **Save this key** - you'll need it in Step 3

### 1.3 Tavily API Key
1. Go to [https://tavily.com/](https://tavily.com/)
2. Click **"Get Started"** or **"Sign Up"**
3. Complete the registration process
4. Go to your **Dashboard**
5. Find your API key in the dashboard
6. Copy the API key
7. **Save this key** - you'll need it in Step 3

---

## 🌐 Step 2: Deploy to Render

### 2.1 Access Render Dashboard
1. Go to [https://dashboard.render.com/](https://dashboard.render.com/)
2. Sign up for a free account or log in
3. You'll see the main dashboard

### 2.2 Create a New Web Service
1. Click the **"New +"** button in the top right
2. Select **"Web Service"** from the dropdown menu
3. You'll be taken to the service creation page

### 2.3 Connect Your GitHub Repository
1. In the **"Source Code"** section:
   - Click **"Connect GitHub"** if not already connected
   - Authorize Render to access your GitHub repositories
2. Find your repository in the list and click **"Connect"**
   - If you can't find it, use the search box
   - Make sure your repository is public

### 2.4 Configure Service Settings
Fill in the following configuration:

**Basic Settings:**
- **Name**: `research-assistant` (or your preferred name)
- **Region**: `Singapore` (closest to India for better performance)
- **Branch**: `main` (or your default branch)

**Build & Deploy Settings:**
- **Environment**: `Docker`
- **Dockerfile Path**: `./Dockerfile` (should auto-detect)

**Instance Settings:**
- **Plan**: `Free` (sufficient for testing and small-scale usage)

### 2.5 Advanced Settings (Optional but Recommended)
1. Scroll down to **"Advanced"** section
2. **Auto-Deploy**: `Yes` (enables automatic deployments when you push to GitHub)
3. **Build Command**: Leave empty (Docker handles this)
4. **Start Command**: Leave empty (defined in Dockerfile)

---

## ⚙️ Step 3: Configure Environment Variables

This is the most critical step. In the **Environment Variables** section:

### 3.1 Add Required Variables
Click **"Add Environment Variable"** for each of the following:

**Variable 1:**
- **Key**: `OPENROUTER_API_KEY`
- **Value**: Your OpenRouter API key from Step 1.1

**Variable 2:**
- **Key**: `OPENROUTER_BASE_URL`
- **Value**: `https://openrouter.ai/api/v1`

**Variable 3:**
- **Key**: `YOUR_SITE_URL`
- **Value**: `https://your-app-name.onrender.com` 
  - Replace `your-app-name` with your actual service name
  - You can update this after deployment with the actual URL

**Variable 4:**
- **Key**: `YOUR_SITE_NAME`
- **Value**: `Personal Research Assistant`

**Variable 5:**
- **Key**: `GROQ_API_KEY`
- **Value**: Your Groq API key from Step 1.2

**Variable 6:**
- **Key**: `TAVILY_API_KEY`
- **Value**: Your Tavily API key from Step 1.3

**Variable 7:**
- **Key**: `PORT`
- **Value**: `8501`

### 3.2 Verify Environment Variables
Double-check that all 7 environment variables are correctly set:
- ✅ OPENROUTER_API_KEY
- ✅ OPENROUTER_BASE_URL
- ✅ YOUR_SITE_URL
- ✅ YOUR_SITE_NAME
- ✅ GROQ_API_KEY
- ✅ TAVILY_API_KEY
- ✅ PORT

---

## 🚀 Step 4: Deploy Your Application

### 4.1 Start Deployment
1. Review all your settings one final time
2. Click the **"Create Web Service"** button
3. Render will start building your application

### 4.2 Monitor Build Process
1. You'll be redirected to your service dashboard
2. Watch the **"Logs"** tab for build progress
3. The build process typically takes 5-10 minutes for first deployment

**Expected Build Stages:**
1. 📥 **Cloning repository** from GitHub
2. 🐳 **Building Docker image** (multi-stage build)
3. 📦 **Installing dependencies** via pip-tools
4. ✅ **Build completed**
5. 🚀 **Starting service**

### 4.3 Verify Successful Deployment
1. Wait for the status to show **"Live"** (green indicator)
2. Click on your service URL (e.g., `https://your-app-name.onrender.com`)
3. You should see the Streamlit interface

---

## 🔧 Step 5: Test Your Application

### 5.1 Basic Functionality Test
1. Access your deployed application
2. Enter a test research topic (e.g., "Benefits of renewable energy")
3. Click **"Start Research"**
4. Verify that:
   - ✅ Research plan is generated
   - ✅ Execution steps show progress
   - ✅ Final report is produced

### 5.2 Update YOUR_SITE_URL (Important!)
1. Go back to your Render service dashboard
2. Go to **"Environment"** tab
3. Find the `YOUR_SITE_URL` variable
4. Update it with your actual Render URL (e.g., `https://research-assistant-xyz.onrender.com`)
5. Click **"Save Changes"**
6. The service will automatically redeploy

---

## 🔄 Step 6: Enable Auto-Deployment (Optional)

### 6.1 Verify Auto-Deploy Settings
1. In your Render service dashboard
2. Go to **"Settings"** tab
3. Ensure **"Auto-Deploy"** is set to **"Yes"**

### 6.2 Test Auto-Deployment
1. Make a small change to your README.md locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "test: verify auto-deployment"
   git push origin main
   ```
3. Watch your Render service automatically redeploy

---

## 📊 Step 7: Monitor Your Application

### 7.1 Access Service Metrics
1. In your Render dashboard, go to **"Metrics"** tab
2. Monitor:
   - **Response Time**
   - **CPU Usage**
   - **Memory Usage**
   - **Request Count**

### 7.2 Check Logs for Issues
1. Go to **"Logs"** tab
2. Monitor for any errors or warnings
3. Common issues to watch for:
   - API key errors
   - Rate limiting issues
   - Memory usage spikes

---

## 🚨 Troubleshooting Common Issues

### Issue 1: Build Fails
**Symptoms:** Build fails during Docker build stage
**Solutions:**
- Check that `Dockerfile` is in repository root
- Verify `requirements.in` has all necessary dependencies
- Check build logs for specific error messages

### Issue 2: Application Won't Start
**Symptoms:** Build succeeds but service shows as "Build failed"
**Solutions:**
- Verify `PORT` environment variable is set to `8501`
- Check that Streamlit is properly configured in Dockerfile
- Review startup logs for Python import errors

### Issue 3: API Errors
**Symptoms:** Application starts but research fails
**Solutions:**
- Verify all API keys are correctly set
- Check API key quotas and limits
- Test API keys individually with simple requests

### Issue 4: Slow Performance
**Symptoms:** Application is very slow to respond
**Solutions:**
- Consider upgrading to a paid Render plan
- Optimize your research queries
- Check if APIs have rate limiting

### Issue 5: Service Goes to Sleep
**Symptoms:** First request after inactivity is very slow
**Solutions:**
- This is normal for free tier (services sleep after 15 minutes of inactivity)
- Consider upgrading to paid plan for always-on service
- Use a service like UptimeRobot to ping your app periodically

---

## 🔧 Step 8: Optional Enhancements

### 8.1 Custom Domain (Paid Plans)
1. Go to **"Settings"** → **"Custom Domains"**
2. Add your domain and configure DNS
3. SSL certificates are automatically managed

### 8.2 Deploy Hooks for CI/CD
1. Go to **"Settings"** → **"Deploy Hooks"**
2. Copy the webhook URL
3. Add as `RENDER_DEPLOY_HOOK_URL` secret in GitHub
4. Enables controlled deployments via GitHub Actions

### 8.3 Database Integration
If you need persistent storage:
1. Create a **PostgreSQL** service in Render
2. Add database connection string to environment variables
3. Modify your application to use database

---

## 📈 Scaling Considerations

### Free Tier Limitations
- **750 hours/month** of runtime
- **Services sleep** after 15 minutes of inactivity
- **Limited CPU/memory** resources
- **No always-on** guarantee

### When to Upgrade
Consider upgrading when you experience:
- Frequent cold starts affecting user experience
- Hitting the 750-hour monthly limit
- Need for guaranteed uptime
- Performance issues under load

---

## 🎉 Congratulations!

Your Personal Research Assistant is now deployed on Render! 

**Your application is available at:** `https://your-service-name.onrender.com`

**Next steps:**
- Share the URL with users
- Monitor performance and usage
- Consider adding features based on user feedback
- Set up monitoring and alerting for production use

---

## 📞 Support Resources

- **Render Documentation**: [https://render.com/docs](https://render.com/docs)
- **Render Community**: [https://community.render.com](https://community.render.com)
- **GitHub Issues**: Create issues in your repository for bugs
- **API Documentation**: 
  - OpenRouter: [https://openrouter.ai/docs](https://openrouter.ai/docs)
  - Groq: [https://console.groq.com/docs](https://console.groq.com/docs)
  - Tavily: [https://docs.tavily.com](https://docs.tavily.com)

---

**Last Updated**: December 2024
**Version**: 1.0