# Static Site Generator Microservice

A flexible static site generator that transforms content files and templates into deployable static websites with support for multiple templating engines and build optimizations.

## Features

- **Multi-format Content**: Markdown, HTML, JSON, YAML content support
- **Template Engines**: Handlebars, Mustache, Liquid, and custom template support
- **Theme System**: Switchable themes with custom styling
- **Asset Pipeline**: CSS/JS minification, image optimization, and bundling
- **Build Optimization**: Fast incremental builds and caching
- **Plugin System**: Extensible architecture with custom plugins
- **SEO Optimization**: Automatic sitemap, meta tags, and structured data

## Technical Stack

- **Template Engine**: Handlebars, Mustache, or custom engine
- **Asset Processing**: Webpack or Parcel for bundling and optimization
- **Content Processing**: Custom parsers for Markdown and front matter
- **File System**: Efficient file watching and incremental builds
- **CDN Integration**: Automatic deployment to CDN providers

## API Endpoints

- `POST /generate` - Generate static site from source files
- `GET /build/{buildId}` - Get build status and results
- `POST /preview` - Generate preview of site changes
- `GET /themes` - List available themes
- `POST /deploy` - Deploy generated site to hosting platform
- `GET /assets` - Manage and optimize site assets

## Content Types

- **Pages**: Static pages with custom layouts
- **Posts**: Blog posts with date-based organization
- **Collections**: Grouped content like portfolios or products
- **Data Files**: JSON/YAML data for dynamic content generation
- **Assets**: Images, CSS, JavaScript, and other static files

## Build Features

- **Incremental Builds**: Only rebuild changed content
- **Asset Optimization**: Image compression, CSS/JS minification
- **Code Splitting**: Separate critical and non-critical resources
- **Progressive Web App**: Service worker and manifest generation
- **Performance**: Lazy loading, critical CSS inlining
- **Accessibility**: Automated accessibility checks and improvements

## Template Features

- **Layouts**: Hierarchical layout system with inheritance
- **Partials**: Reusable template components
- **Helpers**: Custom template functions and filters
- **Data Binding**: Dynamic content from external sources
- **Internationalization**: Multi-language site support
- **Conditional Rendering**: Dynamic content based on data

## Key Learning Objectives

- File processing and transformation pipelines
- Template engine design and implementation
- Build optimization and performance
- Static site architecture patterns
- Asset pipeline and optimization techniques

## Implementation Notes

- Uses file system watching for development server
- Implements intelligent caching for faster builds
- Features plugin architecture for extensibility
- Includes comprehensive error handling and validation
- Supports multiple output formats (HTML, AMP, JSON)

## Deployment Integration

- **Netlify**: Direct integration with Netlify deployment
- **Vercel**: Zero-config deployment to Vercel
- **AWS S3**: Static hosting with CloudFront CDN
- **GitHub Pages**: Automated deployment via GitHub Actions
- **Custom**: Generic deployment via webhooks and APIs 