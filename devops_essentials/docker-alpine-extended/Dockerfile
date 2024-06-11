# Use the official Alpine image from the Docker Hub
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Copy the config.txt file into the container
COPY config.txt /app/config.txt

# Default command
CMD ["echo", "Image built successfully. Use 'docker run <image_name> <command>' to run specific commands."]
