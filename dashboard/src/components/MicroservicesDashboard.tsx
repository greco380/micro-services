'use client'

import React, { useState, useEffect } from 'react';
import { 
  Link, Upload, Clock, FileText, DollarSign, Shield, 
  BarChart3, Settings, Globe, Zap, Image, Mail, 
  Database, CheckCircle, FileJson, Bell, MessageCircle,
  BarChart2, Tag, Flag, User, Webhook, Lock, Youtube,
  X, Play, Pause, RotateCcw, Eye, Download, Send
} from 'lucide-react';

const MicroservicesDashboard = () => {
  const [selectedService, setSelectedService] = useState<string | null>(null);
  const [uploadedFile, setUploadedFile] = useState<any>(null);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [markdownText, setMarkdownText] = useState('# Hello World\n\nThis is **bold** text and this is *italic* text.\n\n## Lists\n- Item 1\n- Item 2\n- Item 3');
  const [convertedHtml, setConvertedHtml] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [longUrl, setLongUrl] = useState('');
  const [loadBalancerDemo, setLoadBalancerDemo] = useState({ running: false, progress: 0, instances: [] as any[] });
  const [authForm, setAuthForm] = useState({ email: '', password: '', mode: 'login' });
  const [currencyForm, setCurrencyForm] = useState({ amount: 100, from: 'USD', to: 'EUR', result: null as number | null });
  const [csvData, setCsvData] = useState('');
  const [jsonResult, setJsonResult] = useState('');
  const [pollData, setPollData] = useState({ question: '', options: ['', ''], votes: [] as any[] });
  const [formData, setFormData] = useState({ email: '', name: '', age: '' });
  const [validationResult, setValidationResult] = useState<any>(null);

  const services = [
    { id: 'url-shortener', name: 'URL Shortener', icon: Link, description: 'Convert long URLs into short, manageable links', type: 'interactive' },
    { id: 'file-uploader', name: 'File Uploader', icon: Upload, description: 'Secure file upload and storage service', type: 'interactive' },
    { id: 'task-scheduler', name: 'Task Scheduler', icon: Clock, description: 'Schedule tasks for future execution', type: 'interactive' },
    { id: 'markdown-converter', name: 'Markdown to HTML', icon: FileText, description: 'Convert Markdown text to HTML', type: 'interactive' },
    { id: 'currency-converter', name: 'Currency Converter', icon: DollarSign, description: 'Convert between different currencies', type: 'interactive' },
    { id: 'auth-service', name: 'Authentication Service', icon: Shield, description: 'User registration and login system', type: 'interactive' },
    { id: 'log-aggregator', name: 'Log Aggregator', icon: BarChart3, description: 'Collect and organize application logs', type: 'demo' },
    { id: 'config-service', name: 'Config Management', icon: Settings, description: 'Centralized configuration management', type: 'demo' },
    { id: 'static-generator', name: 'Static Site Generator', icon: Globe, description: 'Generate static websites from templates', type: 'demo' },
    { id: 'load-balancer', name: 'Load Balancer', icon: Zap, description: 'Distribute workload across multiple instances', type: 'demo' },
    { id: 'image-resizer', name: 'Image Resizer', icon: Image, description: 'Resize images to specified dimensions', type: 'interactive' },
    { id: 'email-service', name: 'Email Notifications', icon: Mail, description: 'Send automated email notifications', type: 'interactive' },
    { id: 'caching-service', name: 'Content Caching', icon: Database, description: 'Cache static content for performance', type: 'demo' },
    { id: 'form-validator', name: 'Form Validator', icon: CheckCircle, description: 'Validate form inputs for security', type: 'interactive' },
    { id: 'csv-converter', name: 'CSV to JSON', icon: FileJson, description: 'Convert CSV files to JSON format', type: 'interactive' },
    { id: 'notification-hub', name: 'Notification Hub', icon: Bell, description: 'Send push notifications to devices', type: 'interactive' },
    { id: 'commenting-system', name: 'Commenting System', icon: MessageCircle, description: 'Manage user comments and discussions', type: 'interactive' },
    { id: 'polling-service', name: 'Polling/Voting', icon: BarChart2, description: 'Create polls and collect votes', type: 'interactive' },
    { id: 'tagging-system', name: 'Tagging System', icon: Tag, description: 'Tag and categorize content', type: 'interactive' },
    { id: 'feature-flags', name: 'Feature Flags', icon: Flag, description: 'Toggle features without code deployment', type: 'demo' },
    { id: 'session-management', name: 'Session Management', icon: User, description: 'Handle user sessions and authentication', type: 'demo' },
    { id: 'webhooks-listener', name: 'Webhooks Listener', icon: Webhook, description: 'Process incoming webhook events', type: 'demo' },
    { id: 'encryption-service', name: 'Data Encryption', icon: Lock, description: 'Encrypt and decrypt sensitive data', type: 'interactive' },
    { id: 'youtube-analyzer', name: 'YouTube Content Analyzer', icon: Youtube, description: 'Analyze viewing habits for creative ideas', type: 'demo' }
  ];

  const convertMarkdownToHtml = (markdown: string) => {
    return markdown
      .replace(/^# (.*$)/gm, '<h1>$1</h1>')
      .replace(/^## (.*$)/gm, '<h2>$1</h2>')
      .replace(/^### (.*$)/gm, '<h3>$1</h3>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/^- (.*$)/gm, '<li>$1</li>')
      .replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>')
      .replace(/\n/g, '<br>');
  };

  const shortenUrl = () => {
    if (longUrl) {
      const shortCode = Math.random().toString(36).substring(2, 8);
      setShortUrl(`https://short.ly/${shortCode}`);
    }
  };

  const startLoadBalancerDemo = () => {
    setLoadBalancerDemo({ running: true, progress: 0, instances: [] });
    
    // Initialize instances
    const instances = [
      { id: 1, name: 'Instance 1', files: [], status: 'ready' },
      { id: 2, name: 'Instance 2', files: [], status: 'ready' },
      { id: 3, name: 'Instance 3', files: [], status: 'ready' }
    ];
    
    // Distribute 50 files across instances
    const files = Array.from({ length: 50 }, (_, i) => ({ 
      id: i + 1, 
      name: `file_${i + 1}.txt`, 
      size: Math.floor(Math.random() * 1000) + 100,
      processed: false 
    }));
    
    // Distribute files evenly
    files.forEach((file, index) => {
      instances[index % 3].files.push(file);
    });
    
    setLoadBalancerDemo(prev => ({ ...prev, instances }));
    
    // Simulate processing
    let progress = 0;
    const interval = setInterval(() => {
      progress += 2;
      setLoadBalancerDemo(prev => ({
        ...prev,
        progress,
        instances: prev.instances.map(instance => ({
          ...instance,
          status: progress < 100 ? 'processing' : 'completed',
          files: instance.files.map((file: any) => ({
            ...file,
            processed: Math.random() < (progress / 100)
          }))
        }))
      }));
      
      if (progress >= 100) {
        clearInterval(interval);
        setLoadBalancerDemo(prev => ({ ...prev, running: false }));
      }
    }, 100);
  };

  const convertCurrency = () => {
    const rates: { [key: string]: number } = { USD: 1, EUR: 0.85, GBP: 0.73, JPY: 110, CAD: 1.25 };
    const result = (currencyForm.amount * rates[currencyForm.to]) / rates[currencyForm.from];
    setCurrencyForm(prev => ({ ...prev, result: Number(result.toFixed(2)) }));
  };

  const convertCsvToJson = () => {
    if (!csvData.trim()) return;
    
    const lines = csvData.trim().split('\n');
    const headers = lines[0].split(',').map(h => h.trim());
    const result = lines.slice(1).map(line => {
      const values = line.split(',').map(v => v.trim());
      const obj: { [key: string]: string } = {};
      headers.forEach((header, index) => {
        obj[header] = values[index] || '';
      });
      return obj;
    });
    
    setJsonResult(JSON.stringify(result, null, 2));
  };

  const validateForm = () => {
    const errors = [];
    if (!formData.email.includes('@')) errors.push('Invalid email format');
    if (!formData.name.trim()) errors.push('Name is required');
    if (formData.age && (isNaN(Number(formData.age)) || Number(formData.age) < 0)) errors.push('Age must be a positive number');
    
    setValidationResult({
      valid: errors.length === 0,
      errors,
      message: errors.length === 0 ? 'Form validation passed!' : 'Form has validation errors'
    });
  };

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:4000/upload');

    setUploadProgress(0);

    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) {
        setUploadProgress(Math.round((e.loaded / e.total) * 100));
      }
    };

    xhr.onload = () => {
      if (xhr.status === 200) {
        setUploadProgress(100);
        try {
          const response = JSON.parse(xhr.responseText);
          const url = response.url;

          if (file.type.startsWith('text/') || file.type === 'application/json') {
            fetch(url)
              .then(res => res.text())
              .then(text => {
                setUploadedFile({
                  name: file.name,
                  size: file.size,
                  type: file.type,
                  url,
                  content: text
                });
              });
          } else {
            setUploadedFile({
              name: file.name,
              size: file.size,
              type: file.type,
              url
            });
          }
        } catch (err) {
          console.error(err);
        }
      }
    };

    xhr.send(formData);
  };

  const renderServiceModal = () => {
    if (!selectedService) return null;

    const service = services.find(s => s.id === selectedService);
    if (!service) return null;
    
    return (
      <div className="modal-overlay">
        <div className="modal-content">
          <div className="modal-header">
            <div className="flex justify-between items-center">
              <div className="flex items-center space-x-3">
                <service.icon className="h-6 w-6 text-blue-600" />
                <h2 className="text-xl font-bold">{service.name}</h2>
              </div>
              <button 
                onClick={() => setSelectedService(null)}
                className="text-gray-500 hover:text-gray-700"
              >
                <X className="h-6 w-6" />
              </button>
            </div>
          </div>
          
          <div className="modal-body">
            {selectedService === 'file-uploader' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">Upload File</h3>
                <p>Please select the file you would like to upload.</p>
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
                  <Upload className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                  <input
                    type="file"
                    onChange={handleFileUpload}
                    className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                  />
                  {uploadProgress > 0 && uploadProgress < 100 && (
                    <progress value={uploadProgress} max="100" className="w-full mt-4"></progress>
                  )}
                </div>
                
                {uploadedFile && (
                  <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                    <h4 className="font-semibold mb-2">File Preview:</h4>
                    <div className="text-sm text-gray-600 mb-2">
                      <p><strong>Name:</strong> {uploadedFile.name}</p>
                      <p><strong>Size:</strong> {(uploadedFile.size / 1024).toFixed(2)} KB</p>
                      <p><strong>Type:</strong> {uploadedFile.type}</p>
                    </div>
                    <div className="mt-3 p-3 bg-white rounded border max-h-40 overflow-y-auto">
                      {uploadedFile.type?.startsWith('image/') ? (
                        <img src={uploadedFile.url} alt={uploadedFile.name} className="max-w-full h-auto" />
                      ) : (
                        <pre className="text-xs whitespace-pre-wrap">{uploadedFile.content}</pre>
                      )}
                    </div>
                  </div>
                )}
              </div>
            )}

            {selectedService === 'url-shortener' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">URL Shortener</h3>
                <div className="space-y-3">
                  <input
                    type="url"
                    placeholder="Enter long URL here..."
                    value={longUrl}
                    onChange={(e) => setLongUrl(e.target.value)}
                    className="input-field"
                  />
                  <button
                    onClick={shortenUrl}
                    className="btn-primary"
                  >
                    Shorten URL
                  </button>
                  {shortUrl && (
                    <div className="p-4 bg-green-50 rounded-lg">
                      <p className="text-sm text-gray-600">Shortened URL:</p>
                      <p className="font-mono text-blue-600 break-all">{shortUrl}</p>
                      <button className="mt-2 text-sm text-blue-600 hover:underline">
                        Copy to clipboard
                      </button>
                    </div>
                  )}
                </div>
              </div>
            )}

            {selectedService === 'markdown-converter' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">Markdown to HTML Converter</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">Markdown Input:</label>
                    <textarea
                      value={markdownText}
                      onChange={(e) => setMarkdownText(e.target.value)}
                      className="textarea-field h-40"
                      placeholder="Enter Markdown here..."
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">HTML Output:</label>
                    <div className="h-40 p-3 border rounded-lg bg-gray-50 overflow-y-auto">
                      <div dangerouslySetInnerHTML={{ __html: convertMarkdownToHtml(markdownText) }} />
                    </div>
                  </div>
                </div>
                <div className="mt-4 p-3 bg-gray-100 rounded-lg">
                  <p className="text-sm font-medium mb-2">Raw HTML:</p>
                  <code className="text-xs text-gray-700 break-all">
                    {convertMarkdownToHtml(markdownText)}
                  </code>
                </div>
              </div>
            )}

            {selectedService === 'currency-converter' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">Currency Converter</h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">Amount:</label>
                    <input
                      type="number"
                      value={currencyForm.amount}
                      onChange={(e) => setCurrencyForm(prev => ({ ...prev, amount: parseFloat(e.target.value) || 0 }))}
                      className="input-field"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">From:</label>
                    <select
                      value={currencyForm.from}
                      onChange={(e) => setCurrencyForm(prev => ({ ...prev, from: e.target.value }))}
                      className="input-field"
                    >
                      <option value="USD">USD</option>
                      <option value="EUR">EUR</option>
                      <option value="GBP">GBP</option>
                      <option value="JPY">JPY</option>
                      <option value="CAD">CAD</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">To:</label>
                    <select
                      value={currencyForm.to}
                      onChange={(e) => setCurrencyForm(prev => ({ ...prev, to: e.target.value }))}
                      className="input-field"
                    >
                      <option value="USD">USD</option>
                      <option value="EUR">EUR</option>
                      <option value="GBP">GBP</option>
                      <option value="JPY">JPY</option>
                      <option value="CAD">CAD</option>
                    </select>
                  </div>
                </div>
                <button
                  onClick={convertCurrency}
                  className="btn-primary"
                >
                  Convert
                </button>
                {currencyForm.result && (
                  <div className="p-4 bg-green-50 rounded-lg">
                    <p className="text-lg font-semibold">
                      {currencyForm.amount} {currencyForm.from} = {currencyForm.result} {currencyForm.to}
                    </p>
                  </div>
                )}
              </div>
            )}

            {selectedService === 'csv-converter' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">CSV to JSON Converter</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">CSV Input:</label>
                    <textarea
                      value={csvData}
                      onChange={(e) => setCsvData(e.target.value)}
                      placeholder="name,age,city&#10;John,25,New York&#10;Jane,30,London"
                      className="textarea-field h-40"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">JSON Output:</label>
                    <pre className="w-full h-40 p-3 border rounded-lg bg-gray-50 overflow-y-auto text-xs">
                      {jsonResult}
                    </pre>
                  </div>
                </div>
                <button
                  onClick={convertCsvToJson}
                  className="btn-primary"
                >
                  Convert to JSON
                </button>
              </div>
            )}

            {selectedService === 'form-validator' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">Form Validator</h3>
                <div className="space-y-3">
                  <div>
                    <label className="block text-sm font-medium mb-2">Email:</label>
                    <input
                      type="email"
                      value={formData.email}
                      onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
                      className="input-field"
                      placeholder="Enter email address"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Name:</label>
                    <input
                      type="text"
                      value={formData.name}
                      onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
                      className="input-field"
                      placeholder="Enter full name"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">Age (optional):</label>
                    <input
                      type="number"
                      value={formData.age}
                      onChange={(e) => setFormData(prev => ({ ...prev, age: e.target.value }))}
                      className="input-field"
                      placeholder="Enter age"
                    />
                  </div>
                  <button
                    onClick={validateForm}
                    className="btn-primary"
                  >
                    Validate Form
                  </button>
                  
                  {validationResult && (
                    <div className={`p-4 rounded-lg ${validationResult.valid ? 'bg-green-50 text-green-800' : 'bg-red-50 text-red-800'}`}>
                      <p className="font-semibold">{validationResult.message}</p>
                      {validationResult.errors.length > 0 && (
                        <ul className="mt-2 list-disc list-inside text-sm">
                          {validationResult.errors.map((error: string, index: number) => (
                            <li key={index}>{error}</li>
                          ))}
                        </ul>
                      )}
                    </div>
                  )}
                </div>
              </div>
            )}

            {selectedService === 'load-balancer' && (
              <div className="space-y-4">
                <h3 className="text-lg font-semibold">Load Balancer Demo</h3>
                <p className="text-gray-600">Watch how 50 text files are distributed across 3 server instances for parallel processing.</p>
                
                <button
                  onClick={startLoadBalancerDemo}
                  disabled={loadBalancerDemo.running}
                  className="btn-primary disabled:opacity-50"
                >
                  {loadBalancerDemo.running ? 'Processing...' : 'Start Demo'}
                </button>

                {loadBalancerDemo.instances.length > 0 && (
                  <div className="space-y-4">
                    <div className="bg-gray-200 rounded-full h-4">
                      <div 
                        className="bg-blue-600 h-4 rounded-full transition-all duration-300"
                        style={{ width: `${loadBalancerDemo.progress}%` }}
                      ></div>
                    </div>
                    <p className="text-center font-semibold">{loadBalancerDemo.progress}% Complete</p>
                    
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      {loadBalancerDemo.instances.map((instance: any) => (
                        <div key={instance.id} className="border rounded-lg p-4">
                          <h4 className="font-semibold mb-2 flex items-center">
                            {instance.name}
                            <span className={`ml-2 px-2 py-1 text-xs rounded ${
                              instance.status === 'ready' ? 'bg-gray-200' :
                              instance.status === 'processing' ? 'bg-yellow-200' : 'bg-green-200'
                            }`}>
                              {instance.status}
                            </span>
                          </h4>
                          <div className="text-sm text-gray-600">
                            <p>Files: {instance.files.length}</p>
                            <p>Processed: {instance.files.filter((f: any) => f.processed).length}</p>
                            <div className="mt-2 max-h-20 overflow-y-auto">
                              {instance.files.slice(0, 5).map((file: any) => (
                                <div key={file.id} className={`text-xs ${file.processed ? 'text-green-600' : 'text-gray-400'}`}>
                                  {file.name} ({file.size}KB) {file.processed ? '✓' : '⏳'}
                                </div>
                              ))}
                              {instance.files.length > 5 && <p className="text-xs text-gray-400">...and {instance.files.length - 5} more</p>}
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Default service display for services without specific implementation */}
            {!['file-uploader', 'url-shortener', 'markdown-converter', 'currency-converter', 'csv-converter', 'form-validator', 'load-balancer'].includes(selectedService) && (
              <div className="text-center py-8">
                <service.icon className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                <h3 className="text-lg font-semibold mb-2">{service.name}</h3>
                <p className="text-gray-600 mb-4">{service.description}</p>
                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                  <p className="text-yellow-800">
                    This {service.type === 'demo' ? 'demo' : 'interactive interface'} is coming soon! 
                    This service would {service.type === 'demo' ? 'demonstrate' : 'provide functionality for'} {service.description.toLowerCase()}.
                  </p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">Microservices Dashboard</h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Explore our collection of microservices with interactive demos and functional interfaces. 
            Click on any service to see it in action or view a demonstration of its capabilities.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {services.map((service) => {
            const IconComponent = service.icon;
            return (
              <div
                key={service.id}
                onClick={() => setSelectedService(service.id)}
                className="service-card"
              >
                <div className="service-card-content">
                  <div className="flex items-center justify-between mb-4">
                    <IconComponent className="service-icon" />
                    <span className={`px-2 py-1 text-xs rounded-full ${
                      service.type === 'interactive' 
                        ? 'badge-interactive' 
                        : 'badge-demo'
                    }`}>
                      {service.type === 'interactive' ? 'Interactive' : 'Demo'}
                    </span>
                  </div>
                  <h3 className="service-title">
                    {service.name}
                  </h3>
                  <p className="service-description">
                    {service.description}
                  </p>
                </div>
                <div className="px-6 pb-6">
                  <div className="flex items-center text-blue-600 text-sm font-medium group-hover:text-blue-700">
                    {service.type === 'interactive' ? (
                      <>
                        <Play className="h-4 w-4 mr-1" />
                        Try it out
                      </>
                    ) : (
                      <>
                        <Eye className="h-4 w-4 mr-1" />
                        View demo
                      </>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div className="mt-16 bg-white rounded-xl shadow-lg p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">About This Dashboard</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h3 className="text-lg font-semibold mb-3">Interactive Services</h3>
              <p className="text-gray-600">
                Services marked as "Interactive" provide fully functional interfaces where you can 
                upload files, convert data, validate forms, and see real results. These simulate 
                actual microservice functionality.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-3">Demo Services</h3>
              <p className="text-gray-600">
                Services marked as "Demo" show visual representations of how the microservice 
                would work in practice, including load balancing, caching mechanisms, and 
                data flow demonstrations.
              </p>
            </div>
          </div>
        </div>
      </div>
      
      {renderServiceModal()}
    </div>
  );
};

export default MicroservicesDashboard;
