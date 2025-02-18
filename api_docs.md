# **Overview**

The **Student Management System** provides RESTful endpoints to manage students, courses, and enrollments, secured with JWT-based authentication. You must first obtain a token from the authentication endpoint and include it in the `Authorization` header (`Bearer` ) for all protected endpoints.

- **Base URL**: `http://127.0.0.1:8000`
    
- **Authentication**: **Bearer Token** via OAuth2
    

---

# **Getting started guide**

## **Usage Flow**

1. **Obtain a Token**:
    
    - `POST /auth/token` with username/password.
        
    - Get the `access_token`.

    - Obtain a JWT access token by providing valid credentials.

    - username: user 
    - password: password


        
2. **Access Protected Endpoints**:
    
    - Include the token in the `Authorization` header:
        
        1. `Authorization: Bearer`
            
3. **Operations**:
    
    - **Create** or **Retrieve** students/courses.
        
    - **Enroll** students in courses.
        
    - **Fetch** a student's enrolled courses.
        