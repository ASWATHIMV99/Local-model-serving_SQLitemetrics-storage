Question Description: Gemini Proxy Server
Problem Statement
You are required to build a Gemini Proxy Server that acts as a middleware between clients and Google's Gemini AI API. The server should provide local serving capabilities, store metrics in an SQLite database, and offer comprehensive API documentation.
Objective
Create a Flask/FastAPI-based proxy server that:

Interfaces with Google's Gemini AI API
Stores usage metrics in an SQLite database
Provides RESTful endpoints for AI text generation
Includes proper error handling and API documentation

Requirements
Core Functionality
1. API Endpoints

POST /gemini/generate: Main endpoint for text generation
GET /health: Health check endpoint
GET /docs: Swagger UI documentation (if using FastAPI)

2. Request/Response Format
Request Body:
json{
  "prompt": {
    "text": "Your prompt text here"
  },
  "generation_config": {
    "temperature": 0.7,
    "max_output_tokens": 100
  }
}
Response Body:
json{
  "text": "Generated AI response text",
  "metrics": {
    "prompt_tokens": 5,
    "completion_tokens": 20,
    "total_tokens": 25
  }
}
3. Database Schema
Create an SQLite database with a table to store metrics:

id (Primary Key, Auto-increment)
timestamp (DateTime)
prompt_tokens (Integer)
completion_tokens (Integer)
total_tokens (Integer)
temperature (Float)
max_output_tokens (Integer)

4. Environment Configuration

Use .env file for sensitive configuration
Required environment variable: GEMINI_API_KEY

Implementation Details
Technical Requirements

Framework: Use Flask or FastAPI
Database: SQLite with appropriate ORM (SQLAlchemy recommended)
Documentation: Swagger/OpenAPI integration
Error Handling: Proper HTTP status codes and error messages
Token Counting: Implement or integrate token counting for metrics
API Integration: Proper integration with Google Gemini API

File Structure Expected
gemini_proxy_server/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── database.py           # Database models and operations
├── gemini_client.py      # Gemini API integration
└── README.md             # Project documentation
Key Components to Implement
1. Gemini API Integration

Initialize Gemini client with API key
Handle API requests and responses
Implement proper error handling for API failures

2. Database Operations

Create SQLite database and tables
Insert metrics after each successful generation
Handle database connection and cleanup

3. Request Validation

Validate incoming JSON requests
Check required fields (prompt.text)
Validate optional parameters (temperature, max_output_tokens)

4. Error Handling

Handle missing API key
Handle invalid requests (400 Bad Request)
Handle API failures (500 Internal Server Error)
Handle rate limiting and quota exceeded errors

Test Cases
Your implementation should pass the following test scenarios:
Test Case 1: Successful Generation

Input: Valid prompt with default parameters
Expected: 200 status code, proper response format, metrics stored in database

Test Case 2: Custom Generation Config

Input: Prompt with custom temperature and max_output_tokens
Expected: 200 status code, AI respects generation config, metrics stored

Test Case 3: Health Check

Input: GET request to /health
Expected: 200 status code, server status information

Test Case 4: Invalid Request

Input: Request missing required prompt.text field
Expected: 400 status code, appropriate error message

Test Case 5: Database Persistence

Input: Multiple generation requests
Expected: All metrics properly stored and retrievable from database

Test Case 6: API Documentation

Input: GET request to /docs
Expected: Swagger UI documentation accessible

Evaluation Criteria
Functionality (40%)

All endpoints work correctly
Proper integration with Gemini API
Database operations function properly

Code Quality (30%)

Clean, readable, and well-structured code
Proper error handling
Appropriate use of design patterns

API Design (20%)

RESTful API design principles
Proper HTTP status codes
Clear request/response formats

Documentation (10%)

Comprehensive API documentation
Clear code comments
Proper README

Bonus Features (Optional)

Rate Limiting: Implement request rate limiting
Authentication: Add API key authentication for clients
Logging: Comprehensive logging for debugging
Metrics Dashboard: Simple web interface to view stored metrics
Async Support: Asynchronous request handling
Docker Support: Containerization with Dockerfile

Constraints

Use Python 3.8 or higher
Database must be SQLite (for simplicity)
Response time should be under 30 seconds for typical requests
Handle at least 10 concurrent requests efficiently

Setup Instructions

Clone the repository
Create and activate a virtual environment
Install dependencies: pip install -r requirements.txt
Set up .env file with your Gemini API key
Run the server: python app.py
Test the endpoints using the provided test cases

Submission Guidelines

Ensure all test cases pass
Include proper error handling
Provide clear documentation
Code should be production-ready quality
Database should be properly initialized on first run
