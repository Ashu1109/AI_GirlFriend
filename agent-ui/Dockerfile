# Frontend Dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY agent-ui/package.json agent-ui/pnpm-lock.yaml ./
RUN corepack enable && corepack prepare pnpm@9.11.0 --activate \
 && pnpm install --frozen-lockfile

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY agent-ui ./
RUN corepack enable && corepack prepare pnpm@9.11.0 --activate \
 && pnpm run build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

# Expose Next.js port
EXPOSE 3000

# Copy built app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# Start the app
CMD ["node", "node_modules/next/dist/bin/next", "start", "-p", "3000"]
