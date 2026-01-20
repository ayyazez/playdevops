# Frontend build-only container
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build the application
RUN npm run build

# This creates the /app/build directory with static files
# These files will be copied to nginx container via volume

# Create a simple web server to serve build files (for testing)
##FROM node:18-alpine

#WORKDIR /app

# Copy built files from builder stage
#COPY --from=builder /app/build ./build

# Install serve to run a simple web server
#RUN npm install -g serve

# Expose port
#EXPOSE 3000

# Serve the build directory
#CMD ["serve", "-s", "build", "-l", "3000"]
