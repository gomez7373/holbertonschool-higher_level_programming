FROM alpine:latest
RUN apk add --no-cache curl
COPY config.txt /app/config.txt
CMD ["sh", "-c", "echo Extended Alpine Image && tail -f /dev/null"]
