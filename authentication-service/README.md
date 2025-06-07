# Authentication Service Microservice

A secure user authentication and authorization service with comprehensive security features, password management, and session handling.

## Features

- **User Registration**: Secure account creation with email verification
- **Login/Logout**: JWT-based authentication with refresh tokens
- **Password Security**: Bcrypt hashing with configurable salt rounds
- **Multi-factor Authentication**: TOTP, SMS, and email-based 2FA
- **Password Reset**: Secure password recovery with time-limited tokens
- **Account Lockout**: Brute force protection with configurable policies
- **OAuth Integration**: Support for Google, GitHub, Facebook OAuth

## Technical Stack

- **Database**: PostgreSQL for user data and session management
- **Hashing**: Bcrypt for password hashing
- **Tokens**: JWT for authentication tokens
- **Cache**: Redis for session storage and rate limiting
- **Email**: SMTP integration for verification and notifications

## API Endpoints

- `POST /register` - User registration
- `POST /login` - User authentication
- `POST /logout` - Session termination
- `POST /refresh` - Token refresh
- `POST /forgot-password` - Password reset request
- `POST /reset-password` - Password reset confirmation
- `GET /profile` - Get user profile
- `PUT /profile` - Update user profile

## Security Features

- **Password Policies**: Configurable complexity requirements
- **Rate Limiting**: Login attempt limitations
- **Account Verification**: Email/SMS verification for new accounts
- **Audit Logging**: Comprehensive security event logging
- **IP Whitelisting**: Optional IP-based access control
- **Device Tracking**: Track and manage user devices
- **Security Headers**: CORS, CSP, and other security headers

## Multi-Factor Authentication

- **TOTP**: Time-based one-time passwords (Google Authenticator compatible)
- **SMS**: SMS-based verification codes
- **Email**: Email-based verification codes
- **Backup Codes**: Recovery codes for account access
- **Biometric**: Integration ready for biometric authentication

## Key Learning Objectives

- Secure password storage and verification
- JWT token management and validation
- Session management and security
- Multi-factor authentication implementation
- Security best practices and compliance

## Implementation Notes

- Implements OWASP security guidelines
- Uses secure random token generation
- Features configurable password policies
- Includes comprehensive input validation
- Supports account linking and social login
- Implements proper error handling without information leakage

## Compliance & Standards

- **GDPR**: Data protection and privacy compliance
- **OWASP**: Security best practices implementation
- **OAuth 2.0**: Standard OAuth implementation
- **PKCE**: Proof Key for Code Exchange support 