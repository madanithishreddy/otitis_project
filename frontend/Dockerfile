# ======================
# 🔨 Stage 1: Build Stage
# ======================
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Install dependencies early to leverage Docker cache
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

# Copy the rest of the project files
COPY . .

# Build the Next.js app
RUN npm run build

# ==========================
# 🚀 Stage 2: Production Run
# ==========================
FROM node:18-alpine AS runner

# Define environment variables
ENV NODE_ENV=production
ENV NEXT_PUBLIC_API_URL=http://localhost:8000

# Set working directory
WORKDIR /app

# Copy only necessary files for production
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/package-lock.json ./package-lock.json
COPY --from=builder /app/next.config.js ./next.config.js

# Install only production dependencies
RUN npm ci --omit=dev --no-audit --no-fund

# Expose the Next.js default port
EXPOSE 3000

# Start the application
CMD ["npm", "run", "dev"]