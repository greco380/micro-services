import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Microservices Dashboard',
  description: 'Interactive dashboard for exploring and testing microservices',
  keywords: ['microservices', 'dashboard', 'API', 'development', 'learning'],
  authors: [{ name: 'Microservices Learning Project' }],
  viewport: 'width=device-width, initial-scale=1',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body className="antialiased">
        {children}
      </body>
    </html>
  )
} 