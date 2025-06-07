# Currency Converter Microservice

A reliable currency conversion service that handles exchange rate calculations with support for real-time rates, historical data, and multi-currency operations.

## Features

- **Real-time Rates**: Integration with external APIs for current exchange rates
- **Historical Data**: Access to historical exchange rate information
- **Multi-currency Support**: Support for 150+ world currencies
- **Batch Conversion**: Convert multiple amounts/currencies simultaneously
- **Rate Caching**: Intelligent caching to reduce API calls and improve performance
- **Custom Rates**: Override with custom exchange rates for specific scenarios
- **Precision Handling**: Accurate decimal calculations with configurable precision

## Technical Stack

- **Database**: PostgreSQL for storing rates and historical data
- **Cache**: Redis for high-performance rate caching
- **External APIs**: Integration with Fixer.io, ExchangeRate-API, or similar
- **Scheduler**: Background jobs for rate updates
- **API**: RESTful endpoints with rate limiting

## API Endpoints

- `GET /rates` - Get current exchange rates
- `POST /convert` - Convert amount between currencies
- `POST /convert/batch` - Batch currency conversions
- `GET /rates/historical` - Get historical exchange rates
- `GET /currencies` - List supported currencies
- `POST /rates/custom` - Set custom exchange rates

## Supported Operations

- **Simple Conversion**: Convert between two currencies
- **Multi-currency**: Convert one amount to multiple target currencies
- **Portfolio Calculation**: Calculate total value of mixed-currency portfolio
- **Trend Analysis**: Analyze currency trends over time periods
- **Arbitrage Detection**: Identify currency arbitrage opportunities

## Key Learning Objectives

- Mathematical precision in financial calculations
- External API integration and error handling
- Caching strategies for frequently accessed data
- Data consistency and synchronization
- Performance optimization for high-frequency operations

## Implementation Notes

- Uses decimal arithmetic to avoid floating-point precision issues
- Implements circuit breaker pattern for external API calls
- Features configurable update intervals for exchange rates
- Includes comprehensive validation for currency codes
- Supports webhook notifications for significant rate changes

## Data Sources

- **Primary**: Real-time exchange rate APIs
- **Fallback**: Cached rates and historical averages
- **Custom**: User-defined rates for specific scenarios
- **Validation**: Cross-reference multiple sources for accuracy 