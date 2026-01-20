# ==============================
# Stage 1: Get frontend build
# ==============================
FROM frontend:latest AS frontend_build
# (this image is built first)

# ==============================
# Stage 2: Nginx
# ==============================
FROM nginx:alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy nginx configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy frontend build from frontend image
COPY --from=frontend_build /app/build /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
