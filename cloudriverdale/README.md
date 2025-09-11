# CloudRiverdale Internship Preparation Project

이 프로젝트는 cloudrivedale(https://www.cloudriverdale.com.au/) 이라는 회사의 면접을 준비하기 위한 프로젝트이다. 아래 키워드들을 다음주까지 학습하고 면접을 준비하는 걸 목표로 한다.

## Project Overview
**CRM Integrated Microservices Platform** - A microservices architecture project that integrates customer management systems with Salesforce CRM

## Development Roadmap & Learning Concepts

### 1. Spring Boot Backend Service Initial Setup
**Concepts Used**: Maven/Gradle, Spring Boot Annotations, Application.properties  
**Learning Purpose**: Master Spring Boot project structure, dependency management, and configuration file setup

  - ✅ 1.1 Project Initialization: Create Spring Boot project using Spring Initializr with dependencies (Spring Web, Spring Data JPA, PostgreSQL Driver, Spring Security)
  - ✅ 1.2 Basic Configuration: Setup application.yml/properties for database connection, logging levels, and project structure (controller, service, repository packages)
  - ✅ 1.3 Application Entry Point: Create main application class with @SpringBootApplication annotation and understand component scanning and auto-configuration

### 2. Database Integration and JPA Configuration
**Concepts Used**: PostgreSQL, Spring Data JPA, Hibernate, Entity  
**Learning Purpose**: Master ORM-based database integration, entity design, and relationship mapping

  - ✅ 2.1 PostgreSQL Database Setup: Install and configure PostgreSQL, create database schema for CRM system, and setup connection pool configuration
  - ✅ 2.2 JPA Configuration: Configure JPA properties in application.yml, setup Hibernate dialect and DDL generation, and configure transaction management
  - ✅ 2.3 Entity Base Classes: Create BaseEntity with common fields (id, createdAt, updatedAt), implement JPA auditing annotations, and setup entity lifecycle callbacks

### 3. Customer Domain Entity Design
**Concepts Used**: Entity, Repository, Service layers  
**Learning Purpose**: Understand Domain-Driven Design (DDD) basics and layered architecture separation

  - 3.1 Customer Entity Design: Create Customer entity with JPA annotations, define relationships (OneToMany, ManyToOne), and implement validation annotations
  - 3.2 Repository Layer Implementation: Create CustomerRepository extending JpaRepository, implement custom query methods using @Query, and add pagination and sorting capabilities
  - 3.3 Service Layer Architecture: Create CustomerService interface and implementation, implement business logic and validation, and setup transaction boundaries with @Transactional

### 4. Customer Management REST API Endpoints
**Concepts Used**: @RestController, REST API endpoints, Dependency Injection  
**Learning Purpose**: Master RESTful API design principles and Spring's dependency injection mechanism

  - 4.1 REST Controller Setup: Create CustomerController with @RestController, implement CRUD operations (GET, POST, PUT, DELETE), and setup proper HTTP status codes and response entities
  - 4.2 Request/Response DTOs: Create CustomerDTO classes for request/response, implement Bean Validation annotations, and setup ModelMapper for entity-DTO conversion
  - 4.3 API Documentation: Integrate Swagger/OpenAPI 3.0, document all endpoints with proper descriptions, and setup API versioning strategy

### 5. JWT-based Authentication System
**Concepts Used**: Spring Security, JWT authentication  
**Learning Purpose**: Build modern web application token-based authentication security system

  - 5.1 Spring Security Configuration: Setup SecurityConfig class with @EnableWebSecurity, configure authentication and authorization rules, and implement password encoding with BCrypt
  - 5.2 JWT Token Implementation: Create JWT utility class for token generation/validation, implement JWT authentication filter, and setup token refresh mechanism
  - 5.3 User Management System: Create User entity and authentication DTOs, implement login/registration endpoints, and setup role-based access control (RBAC)

### 6. Global Exception Handling System
**Concepts Used**: Exception handling, @ControllerAdvice  
**Learning Purpose**: Design application-wide exception handling strategy and consistent error responses

  - 6.1 Custom Exception Classes: Create custom exception hierarchy, implement business-specific exceptions, and setup exception error codes and messages
  - 6.2 Global Exception Handler: Create @ControllerAdvice class for global exception handling, implement specific exception handlers for different scenarios, and setup standardized error response format
  - 6.3 Validation and Error Handling: Implement field validation error handling, setup method argument validation, and create custom validation annotations

### 7. Inversion of Control (IoC) Container Utilization
**Concepts Used**: IoC, @Autowired, Dependency Injection  
**Learning Purpose**: Master Spring's core philosophy of IoC and practical application of dependency injection

  - 7.1 Bean Configuration: Create configuration classes with @Configuration, define custom beans using @Bean annotation, and understand bean lifecycle and scopes
  - 7.2 Dependency Injection Patterns: Implement constructor injection (recommended), compare field injection vs setter injection, and setup conditional bean creation
  - 7.3 Advanced IoC Features: Create custom annotations for dependency injection, implement bean post-processors, and setup profile-specific bean configurations

### 8. Node.js API Gateway Service
**Concepts Used**: Node.js, Express.js, Event-driven/Non-blocking I/O  
**Learning Purpose**: Implement high-performance API gateway based on asynchronous I/O and microservice communication

  - 8.1 Node.js Project Setup: Initialize Node.js project with npm/yarn, setup TypeScript configuration, and configure development environment with nodemon
  - 8.2 Express.js Server Configuration: Create Express application with TypeScript, setup CORS and security middleware, and configure request parsing and compression
  - 8.3 API Gateway Architecture: Implement request routing to microservices, setup load balancing and failover mechanisms, and configure service discovery and health checks

### 9. Express.js Middleware and Routing System
**Concepts Used**: Middleware, REST API routes, npm/yarn  
**Learning Purpose**: Understand Express.js middleware pipeline and modularized routing system

  - 9.1 Custom Middleware Implementation: Create authentication middleware, implement request logging and monitoring, and setup rate limiting and request validation
  - 9.2 Modular Routing System: Create route modules for different resources, implement nested routing patterns, and setup route parameter validation
  - 9.3 Package Management: Configure npm/yarn workspaces, setup dependency management and security auditing, and implement build and deployment scripts

### 10. Asynchronous Programming and Database Integration
**Concepts Used**: Async/Await, Promises, PostgreSQL integration  
**Learning Purpose**: Master JavaScript/TypeScript asynchronous processing patterns and database connection pool management

  - 10.1 Database Connection Setup: Configure PostgreSQL connection with pg library, setup connection pooling and retry logic, and implement database migration system
  - 10.2 Async/Await Patterns: Convert callback-based code to async/await, implement proper error handling with try-catch, and setup concurrent processing with Promise.all
  - 10.3 Database Abstraction Layer: Create repository pattern implementation, implement query builder and ORM-like features, and setup database transaction management

### 11. Node.js JWT Authentication Middleware
**Concepts Used**: JWT authentication, Error handling  
**Learning Purpose**: Implement token-based authentication and authorization system between microservices

  - 11.1 JWT Middleware Implementation: Create JWT verification middleware, implement token extraction from headers/cookies, and setup token refresh and blacklist mechanism
  - 11.2 Authorization Patterns: Implement role-based authorization, create permission-based access control, and setup resource-level authorization
  - 11.3 Security Best Practices: Implement secure token storage, setup CSRF protection, and configure secure cookie settings

### 12. Environment Variables and Configuration Management
**Concepts Used**: Environment variables, dotenv  
**Learning Purpose**: Separate configuration for dev/staging/production environments and security management

  - 12.1 Environment Configuration: Setup .env files for different environments, implement configuration validation, and create environment-specific build processes
  - 12.2 Secret Management: Implement secure secret storage, setup encryption for sensitive data, and configure external secret management integration
  - 12.3 Configuration Patterns: Create configuration object patterns, implement dynamic configuration reloading, and setup configuration backup and versioning

### 13. Real-time WebSocket Server Implementation
**Concepts Used**: WebSockets  
**Learning Purpose**: Build real-time bidirectional communication for customer consultation chat system

  - 13.1 WebSocket Server Setup: Setup Socket.io server with Express, configure WebSocket authentication, and implement connection management and room handling
  - 13.2 Real-time Chat System: Create chat room management, implement message broadcasting and private messaging, and setup message persistence and history
  - 13.3 WebSocket Security and Scalability: Implement WebSocket authentication and authorization, setup horizontal scaling with Redis adapter, and configure connection monitoring and cleanup

### 14. Salesforce CRM Integration Service
**Concepts Used**: Salesforce CRM basics, Implementation, Integration, Data Management  
**Learning Purpose**: Learn external SaaS API integration and CRM data synchronization strategies

  - 14.1 Salesforce API Setup: Setup Salesforce Developer account and connected app, configure OAuth 2.0 authentication flow, and implement Salesforce REST API client
  - 14.2 Data Synchronization: Create bidirectional data sync between systems, implement conflict resolution strategies, and setup incremental sync with change detection
  - 14.3 CRM Integration Patterns: Implement webhook handling for real-time updates, create bulk data import/export functionality, and setup error handling and retry mechanisms

### 15. Microservices Architecture Integration
**Concepts Used**: Microservices  
**Learning Purpose**: Resolve microservice operational issues like inter-service communication, data consistency, and failure handling

  - 15.1 Service Discovery and Communication: Implement service registry pattern, setup API gateway routing and load balancing, and configure circuit breaker pattern for fault tolerance
  - 15.2 Data Consistency Patterns: Implement saga pattern for distributed transactions, setup event sourcing for data consistency, and create eventual consistency handling
  - 15.3 Monitoring and Observability: Setup distributed tracing with correlation IDs, implement centralized logging aggregation, and create health check endpoints and monitoring dashboards

### 16. MCP (Model Context Protocol) Based AI Agent Integration
**Concepts Used**: MCP, Agentic AI development  
**Learning Purpose**: Implement intelligent CRM functionality using next-generation AI agent development protocols

  - 16.1 MCP Protocol Implementation: Setup MCP server and client communication, implement context management for AI agents, and create tool definition and execution framework
  - 16.2 AI Agent Development: Create customer service AI agent, implement natural language processing for queries, and setup agent memory and context persistence
  - 16.3 Advanced AI Integration: Implement multi-agent coordination, setup agent training and feedback loops, and create AI-powered analytics and insights

## Project Structure
```
cloudriverdale-crm/
├── backend-spring/          # Spring Boot Backend Service
│   ├── src/main/java/
│   │   ├── controller/      # REST Controllers
│   │   ├── service/         # Business Logic Services
│   │   ├── repository/      # Data Access Layer
│   │   ├── entity/          # JPA Entities
│   │   ├── dto/            # Data Transfer Objects
│   │   ├── config/         # Configuration Classes
│   │   └── exception/      # Exception Handling
│   ├── src/main/resources/
│   │   ├── application.yml
│   │   └── db/migration/   # Database Migrations
│   └── pom.xml
├── api-gateway-node/        # Node.js API Gateway
│   ├── src/
│   │   ├── controllers/    # Route Controllers
│   │   ├── middleware/     # Express Middleware
│   │   ├── services/       # Business Services
│   │   ├── utils/          # Utility Functions
│   │   └── config/         # Configuration
│   ├── package.json
│   ├── tsconfig.json
│   └── .env
├── salesforce-integration/  # Salesforce Integration Service
│   ├── src/
│   │   ├── api/           # Salesforce API Client
│   │   ├── sync/          # Data Synchronization
│   │   └── webhooks/      # Webhook Handlers
│   └── package.json
├── mcp-agent/              # MCP AI Agent Service
│   ├── src/
│   │   ├── agents/        # AI Agent Implementations
│   │   ├── tools/         # Agent Tools
│   │   └── protocol/      # MCP Protocol Implementation
│   └── package.json
└── docs/                   # Development Documentation
    ├── api/               # API Documentation
    ├── architecture/      # Architecture Diagrams
    └── interview/         # Interview Questions
```

## Core Features
1. **Customer Management System** - CRUD operations and advanced search
2. **JWT-based Authentication** - Token issuance, renewal, and validation
3. **Real-time Chat** - Customer consultation via WebSocket
4. **Salesforce Synchronization** - Bidirectional CRM data sync
5. **AI Agent Integration** - MCP-based intelligent customer service

## Learning Objectives
- Complete understanding of Spring Boot ecosystem
- Master Node.js asynchronous programming
- Design and implement microservices architecture
- Gain experience with enterprise CRM system integration
- Understand latest AI development trends (MCP)