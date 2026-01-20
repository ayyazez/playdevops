# nginx/Dockerfile
FROM nginx:alpine

# Remove default configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY default.conf /etc/nginx/conf.d/default.conf

# Expose HTTP port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
