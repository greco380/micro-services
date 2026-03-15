FROM node:18-alpine
WORKDIR /app
COPY server/package*.json ./server/
RUN cd server && npm install --production
COPY server ./server
WORKDIR /app/server
EXPOSE 4000
CMD ["node", "server.js"]
