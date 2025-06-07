# Markdown to HTML Converter Microservice

A high-performance text processing service that converts Markdown content to HTML with support for extensions and custom rendering options.

## Features

- **Standard Markdown**: Full CommonMark specification support
- **Extensions**: Tables, footnotes, task lists, syntax highlighting
- **Custom Themes**: CSS theme support with dark/light mode options
- **Sanitization**: HTML sanitization to prevent XSS attacks
- **Math Support**: LaTeX math rendering with MathJax/KaTeX
- **Batch Processing**: Convert multiple documents simultaneously
- **Template Integration**: Custom HTML templates and layouts

## Technical Stack

- **Parser**: Custom markdown parser or integration with marked/markdown-it
- **Sanitizer**: DOMPurify for HTML sanitization
- **Syntax Highlighting**: Prism.js or Highlight.js integration
- **Cache**: Redis for caching frequently converted content
- **API**: RESTful endpoints with streaming support

## API Endpoints

- `POST /convert` - Convert markdown to HTML
- `POST /convert/batch` - Batch markdown conversion
- `GET /preview/{documentId}` - Preview converted content
- `POST /validate` - Validate markdown syntax
- `GET /themes` - List available CSS themes
- `POST /custom-render` - Convert with custom rendering options

## Supported Extensions

- **Tables**: GitHub-flavored table syntax
- **Task Lists**: Interactive checkboxes
- **Footnotes**: Reference-style footnotes
- **Code Blocks**: Syntax highlighting for 100+ languages
- **Math**: Inline and block mathematical expressions
- **Mermaid**: Diagram and flowchart rendering
- **Emoji**: Shortcode emoji support

## Key Learning Objectives

- Text parsing and Abstract Syntax Tree (AST) manipulation
- Regular expression patterns and string processing
- HTML generation and DOM manipulation
- Security considerations in text processing
- Performance optimization for large documents

## Implementation Notes

- Implements streaming processing for large documents
- Uses worker threads for CPU-intensive parsing
- Supports plugin architecture for custom extensions
- Includes comprehensive error handling and validation
- Features configurable output formats (HTML, PDF, etc.)

## Security Features

- **XSS Prevention**: Comprehensive HTML sanitization
- **Input Validation**: Markdown syntax validation
- **Resource Limits**: File size and processing time limits
- **Safe Mode**: Disable potentially dangerous features 