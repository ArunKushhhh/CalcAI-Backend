# CalcAI Backend 🔧⚡

The backend API service for CalcAI - an intelligent calculator application that provides mathematical computation capabilities with AI-powered problem solving through RESTful endpoints.

## 🚀 Overview

This backend service handles complex mathematical calculations, expression parsing, and AI-enhanced computation requests from the CalcAI frontend application. It provides a robust REST API with endpoints for various mathematical operations and intelligent problem-solving capabilities.

## ✨ Features

- **RESTful API**: Clean, well-documented endpoints for mathematical operations
- **Expression Parsing**: Advanced mathematical expression evaluation
- **AI Integration**: Intelligent problem-solving and step-by-step solutions  
- **Real-time Calculations**: Fast computation with optimized algorithms
- **History Management**: Store and retrieve calculation history
- **Error Handling**: Comprehensive error responses and validation
- **CORS Support**: Cross-origin resource sharing for frontend integration
- **Rate Limiting**: API protection against abuse
- **Authentication**: Secure API access (if applicable)
- **Logging**: Comprehensive request and error logging

## 🛠️ Tech Stack

- **Runtime**: Node.js (v16+)
- **Framework**: Express.js
- **Language**: JavaScript/TypeScript
- **Database**: MongoDB/PostgreSQL (for calculation history)
- **AI Integration**: OpenAI API / Custom ML models
- **Validation**: Joi/Express-validator
- **Testing**: Jest/Mocha
- **Documentation**: Swagger/OpenAPI
- **Deployment**: Docker containerization ready

## 📦 Installation

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn
- Database (MongoDB/PostgreSQL)
- API keys for AI services (if applicable)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArunKushhhh/CalcAI-Backend.git
   cd CalcAI-Backend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Configure Environment Variables**
   ```env
   # Server Configuration
   PORT=3001
   NODE_ENV=development
   
   # Database
   DATABASE_URL=mongodb://localhost:27017/calcai
   # or for PostgreSQL
   # DATABASE_URL=postgresql://username:password@localhost:5432/calcai
   
   # AI Service Configuration
   OPENAI_API_KEY=your_openai_api_key
   AI_SERVICE_URL=https://api.openai.com/v1
   
   # Security
   JWT_SECRET=your_jwt_secret_key
   CORS_ORIGIN=http://localhost:5173
   
   # Rate Limiting
   RATE_LIMIT_WINDOW_MS=900000
   RATE_LIMIT_MAX_REQUESTS=100
   ```

5. **Start the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

The API will be available at `http://localhost:3001`

## 🔗 API Endpoints

### Basic Calculator Operations

#### Calculate Expression
```http
POST /api/calculate
Content-Type: application/json

{
  "expression": "2 + 3 * 4",
  "type": "basic"
}
```

**Response:**
```json
{
  "success": true,
  "result": 14,
  "expression": "2 + 3 * 4",
  "steps": ["2 + 12", "14"]
}
```

#### Advanced Mathematical Operations
```http
POST /api/calculate/advanced
Content-Type: application/json

{
  "expression": "sqrt(16) + log(100)",
  "type": "scientific"
}
```

### AI-Enhanced Features

#### Solve Complex Problems
```http
POST /api/ai/solve
Content-Type: application/json

{
  "problem": "If a train travels 120 km in 2 hours, what is its average speed?",
  "context": "physics"
}
```

**Response:**
```json
{
  "success": true,
  "solution": "60 km/h",
  "explanation": "Speed = Distance ÷ Time = 120 km ÷ 2 h = 60 km/h",
  "steps": [
    "Identify given values: Distance = 120 km, Time = 2 hours", 
    "Apply speed formula: Speed = Distance ÷ Time",
    "Calculate: 120 ÷ 2 = 60 km/h"
  ]
}
```

#### Natural Language Processing
```http
POST /api/ai/parse
Content-Type: application/json

{
  "query": "What is twenty-five percent of eighty?",
  "language": "en"
}
```

### History Management

#### Get Calculation History
```http
GET /api/history?limit=10&offset=0
Authorization: Bearer <token>
```

#### Save Calculation
```http
POST /api/history
Content-Type: application/json

{
  "expression": "2^8",
  "result": 256,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Health Check
```http
GET /api/health
```

## 📁 Project Structure

```
CalcAI-Backend/
├── src/
│   ├── controllers/
│   │   ├── calculatorController.js
│   │   ├── aiController.js
│   │   ├── historyController.js
│   │   └── healthController.js
│   ├── middleware/
│   │   ├── auth.js
│   │   ├── rateLimiter.js
│   │   ├── validation.js
│   │   └── errorHandler.js
│   ├── models/
│   │   ├── Calculation.js
│   │   └── User.js
│   ├── routes/
│   │   ├── calculator.js
│   │   ├── ai.js
│   │   ├── history.js
│   │   └── index.js
│   ├── services/
│   │   ├── calculatorService.js
│   │   ├── aiService.js
│   │   └── databaseService.js
│   ├── utils/
│   │   ├── mathUtils.js
│   │   ├── validators.js
│   │   └── logger.js
│   ├── config/
│   │   ├── database.js
│   │   └── environment.js
│   └── app.js
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
│   ├── api.md
│   └── swagger.yaml
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example
├── package.json
├── server.js
└── README.md
```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test suite
npm run test:unit
npm run test:integration
```

### Test Coverage
- Controllers: Unit tests for all API endpoints
- Services: Business logic validation
- Middleware: Authentication and validation testing
- Integration: End-to-end API testing

## 🚀 Deployment

### Using Docker

1. **Build the Docker image**
   ```bash
   docker build -t calcai-backend .
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

### Manual Deployment

1. **Build for production**
   ```bash
   npm run build
   ```

2. **Start production server**
   ```bash
   npm start
   ```

### Environment-Specific Deployment

#### Heroku
```bash
# Login to Heroku
heroku login

# Create app
heroku create calcai-backend-api

# Set environment variables
heroku config:set NODE_ENV=production
heroku config:set DATABASE_URL=your_production_db_url

# Deploy
git push heroku main
```

#### AWS/DigitalOcean
- Use PM2 for process management
- Set up reverse proxy with Nginx
- Configure SSL certificates
- Set up monitoring and logging

## 📊 Performance & Monitoring

### Metrics Tracked
- API response times
- Request success/failure rates
- AI service response times
- Database query performance
- Memory and CPU usage

### Logging
- Request/response logging
- Error tracking and alerting
- Performance monitoring
- Security audit logs

## 🔐 Security

### Implemented Security Measures
- **Rate Limiting**: Prevent API abuse
- **Input Validation**: Sanitize all inputs
- **CORS Configuration**: Secure cross-origin requests
- **Authentication**: JWT-based user authentication
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Input sanitization

### Security Best Practices
- Regular dependency updates
- Environment variable protection
- API key rotation
- Security headers implementation
- Request size limiting

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Workflow
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Write tests** for your changes
4. **Make your changes** following the coding standards
5. **Run tests**: `npm test`
6. **Update documentation** if needed
7. **Commit changes**: `git commit -m 'Add amazing feature'`
8. **Push to branch**: `git push origin feature/amazing-feature`
9. **Open a Pull Request**

### Code Standards
- Follow ESLint configuration
- Write unit tests for new features
- Use meaningful commit messages
- Document API changes
- Maintain backwards compatibility

## 📜 API Documentation

Complete API documentation is available at:
- **Swagger UI**: `http://localhost:3001/api-docs` (when running locally)
- **Postman Collection**: Available in `/docs` folder
- **OpenAPI Spec**: `/docs/swagger.yaml`

## 🐛 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Kill process using port 3001
lsof -ti:3001 | xargs kill -9
```

**Database connection issues**
- Verify database URL in `.env`
- Ensure database server is running
- Check network connectivity

**AI service errors**
- Verify API keys are correctly set
- Check service rate limits
- Monitor service status

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Arun Kush**
- GitHub: [@ArunKushhhh](https://github.com/ArunKushhhh)
- Frontend: [CalcAI](https://github.com/ArunKushhhh/CalcAI)
- Backend: [CalcAI-Backend](https://github.com/ArunKushhhh/CalcAI-Backend)

## 🙏 Acknowledgments

- Express.js community for the robust framework
- OpenAI for AI integration capabilities
- MongoDB/PostgreSQL teams for reliable database solutions
- Open-source contributors and maintainers

## 📞 Support

For support and questions:
- **Issues**: Open an issue on GitHub
- **Documentation**: Check the `/docs` folder
- **API Questions**: Refer to Swagger documentation
- **Bugs**: Report with reproduction steps

---

<div align="center">
  <p>🔧 Built with Node.js and ❤️ by Arun Kush</p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>