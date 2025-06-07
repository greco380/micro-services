# Microservices Dashboard

An interactive web dashboard for exploring and testing all 24 microservices in this learning project. Built with Next.js, TypeScript, and Tailwind CSS.

## 🚀 Features

### Interactive Services
Experience fully functional interfaces for:
- **File Uploader** - Upload and preview files with drag & drop
- **URL Shortener** - Convert long URLs to short links
- **Markdown to HTML Converter** - Real-time markdown conversion
- **Currency Converter** - Convert between major currencies
- **CSV to JSON Converter** - Transform CSV data to JSON format
- **Form Validator** - Validate forms with real-time feedback
- **And more...** - Additional interactive services coming soon

### Demo Services
Visual demonstrations of:
- **Load Balancer** - Watch file distribution across server instances
- **Log Aggregator** - See how logs are collected and processed
- **Config Management** - Configuration distribution visualization
- **Content Caching** - Cache performance demonstrations
- **And others...** - More visual demos for complex services

## 🛠 Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS with custom components
- **Icons**: Lucide React icons
- **Deployment**: Vercel (recommended)

## 📦 Installation

### Prerequisites
- Node.js 18 or higher
- npm or yarn package manager

### Setup Steps

1. **Navigate to the dashboard directory**
   ```bash
   cd dashboard
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

4. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🏗 Project Structure

```
dashboard/
├── src/
│   ├── app/
│   │   ├── globals.css       # Global styles and Tailwind imports
│   │   ├── layout.tsx        # Root layout component
│   │   └── page.tsx          # Home page
│   └── components/
│       └── MicroservicesDashboard.tsx  # Main dashboard component
├── public/                   # Static assets
├── package.json             # Dependencies and scripts
├── tailwind.config.js       # Tailwind CSS configuration
├── tsconfig.json           # TypeScript configuration
└── next.config.js          # Next.js configuration
```

## 🎨 Design Features

### Responsive Grid Layout
- Adaptive grid that works on mobile, tablet, and desktop
- Hover effects and smooth transitions
- Beautiful gradient background

### Interactive Modals
- Full-screen modals for each service
- Service-specific interfaces and demos
- Easy navigation with close buttons

### Visual Indicators
- Color-coded badges for Interactive vs Demo services
- Service icons from Lucide React
- Clear call-to-action buttons

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## 🚀 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy automatically with zero configuration

### Other Platforms
The dashboard can be deployed to any platform that supports Next.js:
- Netlify
- AWS Amplify
- Railway
- Docker containers

## 🎯 Usage Guide

### Exploring Services
1. **Browse the grid** - Each card represents a microservice
2. **Click any service** - Opens a detailed modal interface
3. **Try interactive features** - Upload files, convert data, validate forms
4. **View demos** - Watch visual representations of complex services

### Service Types
- **Green badges** - Interactive services you can actually use
- **Blue badges** - Demo services showing visual representations

### Interactive Examples
- **File Upload**: Try uploading text files, images, or JSON files
- **URL Shortener**: Enter any long URL to see it shortened
- **Markdown Converter**: Edit markdown on the left, see HTML on the right
- **Currency Converter**: Convert between USD, EUR, GBP, JPY, and CAD
- **CSV Converter**: Paste CSV data and see it converted to JSON
- **Form Validator**: Test email validation and form requirements

## 🔮 Future Enhancements

- [ ] Add more interactive service implementations
- [ ] Integrate with actual microservice APIs
- [ ] Add user authentication demo
- [ ] Real-time data updates via WebSockets
- [ ] Performance monitoring dashboard
- [ ] API documentation integration
- [ ] Mobile app companion

## 🤝 Contributing

This dashboard is part of the larger microservices learning project. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational purposes as part of the microservices learning project.

---

**Ready to explore microservices?** Start the development server and dive into the interactive world of distributed systems! 🎉 