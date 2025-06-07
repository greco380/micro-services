# Task Scheduler Microservice

A robust job scheduling service that executes tasks at specific times with support for complex scheduling patterns and distributed execution.

## Features

- **Flexible Scheduling**: Cron expressions, intervals, one-time jobs, and custom schedules
- **Distributed Execution**: Scale across multiple worker instances
- **Job Queues**: Priority-based task queuing with retry mechanisms
- **Monitoring**: Real-time job status tracking and execution history
- **Dead Letter Queue**: Handle failed jobs with configurable retry policies
- **Timezone Support**: Schedule jobs across different time zones
- **Resource Management**: CPU and memory limits for job execution

## Technical Stack

- **Job Queue**: Redis with Bull/BullMQ for job management
- **Database**: PostgreSQL for job definitions and execution history
- **Scheduler**: Custom cron engine with timezone support
- **Workers**: Distributed worker pool with auto-scaling
- **Monitoring**: Prometheus metrics and health checks

## API Endpoints

- `POST /jobs` - Create a new scheduled job
- `GET /jobs` - List all jobs with filtering
- `GET /jobs/{jobId}` - Get job details and status
- `PUT /jobs/{jobId}` - Update job configuration
- `DELETE /jobs/{jobId}` - Cancel a scheduled job
- `POST /jobs/{jobId}/trigger` - Manually trigger job execution

## Job Types

- **HTTP Jobs**: Make HTTP requests to external APIs
- **Script Jobs**: Execute custom scripts or code
- **Database Jobs**: Run database queries or procedures
- **File Jobs**: Process files or perform file operations
- **Webhook Jobs**: Send webhook notifications

## Key Learning Objectives

- Time-based job scheduling algorithms
- Distributed system coordination
- Concurrency management and thread safety
- Fault tolerance and retry mechanisms
- Performance optimization for high-throughput scenarios

## Implementation Notes

- Uses Redis for distributed locking to prevent duplicate execution
- Implements exponential backoff for failed job retries
- Supports job chaining and dependencies
- Includes comprehensive logging and audit trails
- Features graceful shutdown and job recovery mechanisms 