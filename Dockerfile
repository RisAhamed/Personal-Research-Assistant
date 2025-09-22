# Stage 1: Builder
# Use a full OS image to build dependencies
FROM python:3.11 as builder

WORKDIR /app

# Install pip-tools
RUN pip install pip-tools

# Copy only the requirements files to leverage Docker layer caching
COPY requirements.in .
RUN pip-compile requirements.in -o requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final Image
# Use a slim image for the final product
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy installed packages from the builder stage
COPY --from=builder /install /usr/local

# Copy the application source code
COPY ./src ./src

# Change ownership to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Expose the port that Render will provide
EXPOSE ${PORT:-8501}

# Set the command to run the application
# Note: Render provides PORT environment variable, Streamlit binds to it
CMD streamlit run src/main.py --server.port ${PORT:-8501} --server.address 0.0.0.0 --server.headless true --server.fileWatcherType none