# URL Shortener Microservice

A scalable microservice that converts long URLs into shorter, unique versions with tracking capabilities.

## Features

- **URL Shortening**: Convert long URLs into compact, shareable links
- **Custom Aliases**: Allow users to create custom short URLs
- **Analytics**: Track click counts, geographic data, and referrer information
- **Expiration**: Set expiration dates for temporary links
- **Bulk Operations**: Shorten multiple URLs at once
- **QR Code Generation**: Generate QR codes for shortened URLs

## Technical Stack

- **Database**: PostgreSQL for URL storage and analytics
- **Cache**: Redis for high-performance lookups
- **API**: RESTful endpoints with rate limiting
- **Security**: Input validation and spam protection

## API Endpoints

- `POST /shorten` - Create a new short URL
- `GET /{shortCode}` - Redirect to original URL
- `GET /analytics/{shortCode}` - Get click analytics
- `DELETE /{shortCode}` - Delete a short URL
- `POST /bulk` - Bulk URL shortening

## Key Learning Objectives

- Database design and indexing strategies
- URL routing and HTTP redirects
- Caching strategies for high-traffic scenarios
- Analytics data collection and processing
- Rate limiting and abuse prevention

## Implementation Notes

- Uses base62 encoding for short codes
- Implements bloom filters for duplicate detection
- Supports custom domains and vanity URLs
- Includes comprehensive logging and monitoring 