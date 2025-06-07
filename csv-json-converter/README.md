# CSV to JSON Converter Microservice

A robust data transformation service that converts CSV files to JSON format with advanced parsing options, data validation, and batch processing capabilities.

## Features

- **Flexible Parsing**: Handle various CSV formats and delimiters
- **Data Type Inference**: Automatically detect and convert data types
- **Custom Mapping**: Define custom field mappings and transformations
- **Batch Processing**: Process multiple files simultaneously
- **Data Validation**: Validate data integrity during conversion
- **Schema Generation**: Automatically generate JSON schemas
- **Error Handling**: Comprehensive error reporting and recovery

## Technical Stack

- **Parser**: CSV parsing with configurable options
- **Queue**: Redis Bull for batch job processing
- **Storage**: S3-compatible storage for input/output files
- **Database**: PostgreSQL for job tracking and metadata
- **Validation**: JSON Schema validation for output

## API Endpoints

- `POST /convert` - Convert single CSV file to JSON
- `POST /convert/batch` - Batch CSV conversion
- `GET /job/{jobId}` - Get conversion job status
- `POST /validate` - Validate CSV before conversion
- `GET /schema/{fileId}` - Generate JSON schema from CSV
- `POST /transform` - Apply custom transformations

## Conversion Features

- **Header Detection**: Automatic header row detection
- **Data Type Conversion**: String, number, boolean, date conversion
- **Nested JSON**: Convert flat CSV to nested JSON structures
- **Array Handling**: Convert delimited values to arrays
- **Custom Delimiters**: Support various separators and quotes
- **Encoding Support**: UTF-8, Latin-1, and other character encodings

## Data Transformation

- **Field Mapping**: Rename and restructure fields
- **Value Transformation**: Apply functions to data values
- **Conditional Logic**: Transform based on field conditions
- **Aggregation**: Group and aggregate data during conversion
- **Filtering**: Include/exclude rows based on criteria
- **Normalization**: Clean and standardize data formats

## Validation Features

- **Schema Validation**: Validate against predefined schemas
- **Data Quality Checks**: Identify missing or invalid data
- **Duplicate Detection**: Find and handle duplicate records
- **Format Validation**: Ensure proper data formats
- **Business Rules**: Apply domain-specific validation rules
- **Error Reporting**: Detailed validation error reports

## Key Learning Objectives

- Data parsing and transformation techniques
- File processing and streaming I/O
- Data validation and quality assurance
- Batch processing patterns
- Error handling in data pipelines

## Implementation Notes

- Uses streaming for memory-efficient processing of large files
- Implements configurable parsing options for different CSV formats
- Features comprehensive error handling and recovery mechanisms
- Includes progress tracking for long-running conversions
- Supports webhook notifications for batch job completion 