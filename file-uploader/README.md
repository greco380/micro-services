# File Uploader Microservice

A secure and scalable file upload service with support for multiple storage backends and file processing capabilities.

## Features

- **Multi-format Support**: Handle images, documents, videos, and other file types
- **Storage Options**: Local filesystem, AWS S3, Google Cloud Storage, Azure Blob
- **File Validation**: MIME type checking, file size limits, virus scanning
- **Image Processing**: Automatic thumbnail generation and format conversion
- **Chunked Uploads**: Support for large file uploads with resume capability
- **Metadata Extraction**: Extract and store file metadata (EXIF, document properties)
- **Access Control**: Public/private files with permission management

## Technical Stack

- **Storage**: Multi-cloud storage abstraction layer
- **Database**: PostgreSQL for file metadata and permissions
- **Queue**: Redis/RabbitMQ for background processing
- **Security**: File type validation, virus scanning, encryption at rest

## API Endpoints

- `POST /upload` - Upload single file
- `POST /upload/chunked` - Chunked file upload
- `GET /files/{fileId}` - Download file
- `GET /files/{fileId}/metadata` - Get file information
- `DELETE /files/{fileId}` - Delete file
- `POST /files/batch` - Batch file operations

## Security Features

- **Virus Scanning**: Integration with ClamAV or similar
- **File Type Validation**: Whitelist/blacklist approach
- **Size Limits**: Configurable per file type
- **Access Control**: JWT-based authentication
- **Encryption**: Files encrypted at rest and in transit

## Key Learning Objectives

- Secure file handling and validation
- Multi-cloud storage integration
- Background job processing
- Stream processing for large files
- Security best practices for file uploads

## Implementation Notes

- Implements clean architecture with storage abstraction
- Uses worker queues for CPU-intensive operations
- Supports file deduplication to save storage
- Includes comprehensive audit logging 

## Docker Usage

To build and run the Node.js uploader service with Docker:

```bash
docker build -t file-uploader .
docker run -p 4000:4000 file-uploader
```

The server listens on port `4000` by default and stores uploaded files inside the `server/uploads` directory which is exposed at `/uploads`.
