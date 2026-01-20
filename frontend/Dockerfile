# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Install 'serve' globally to serve static build
RUN npm install -g serve

# Build frontend
RUN npm run build

# Expose port for Node server
EXPOSE 3000

# Serve the build directory
CMD ["serve", "-s", "build", "-l", "3000"]
