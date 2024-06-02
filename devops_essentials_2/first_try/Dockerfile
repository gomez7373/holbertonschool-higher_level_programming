# Use the same Alpine base image as the previous exercise
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Add the configuration file to a suitable location in the container
COPY config.txt /app/config.txt

# Set the default command to run when the container starts
CMD ["sh", "-c", "trap 'echo BYE! && exit 0' INT; echo Extended Alpine Image; tail -f /dev/null"]
