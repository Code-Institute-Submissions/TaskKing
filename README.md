# TaskKing

TaskKing is a robust and well-structured Django project designed to streamline task management with a focus on **clean architecture**, **intuitive user interfaces**, and **modern design elements**. It provides a dynamic and engaging user experience while maintaining the flexibility and scalability required for future enhancements.

---

## **Features and Functionalities**

### **1. User Authentication**
- **Dedicated Login System**: 
  - Secure login functionality for registered users.
  - Session management to ensure secure access across multiple devices.
- **User Registration**: 
  - New users can register with a simple form, validated both client-side and server-side.
  - Password hashing for enhanced security.

---

### **2. Task Management**
- **Centralized Task Interface**:
  - Users can view all tasks on a single, clean page (`task_list.html`).
  - Tasks are displayed in a categorized, user-friendly layout.
- **CRUD Operations**:
  - Create, read, update, and delete tasks easily with interactive buttons.
- **Task Prioritization**:
  - Assign priority levels to tasks (e.g., High, Medium, Low) with color-coded indicators.
- **Search and Filter**:
  - Search tasks by keywords.
  - Filter tasks based on their status (e.g., Completed, Pending, In Progress).

---

### **3. Responsive Design**
- **Mobile-Friendly**:
  - Fully responsive templates to ensure seamless use on mobile devices, tablets, and desktops.
- **Cross-Browser Compatibility**:
  - Tested and optimized for modern browsers like Chrome, Firefox, Safari, and Edge.

---

## **Project Structure**

### **Frontend Architecture**

#### **Templates**
| **Template**    | **Description**                      |
|-----------------|--------------------------------------|
| `login.html`    | User authentication page             |
| `register.html` | User registration page               |
| `task_list.html`| Main interface for task management   |

#### **Static Assets**
- **`custom.css`**: Defines the overall look and feel of the project with a focus on modern design principles.
- **`custom.js`**: Adds dynamic functionality, including animations, form validation, and interactive elements.
- **Admin-Specific Assets**: CSS, JavaScript, and images tailored for the admin interface, stored in organized directories.

---

### **Backend Structure**

#### **Core Components**
| **File**        | **Purpose**                                      |
|-----------------|--------------------------------------------------|
| `models.py`     | Defines the database models for tasks and users   |
| `views.py`      | Handles business logic and data rendering         |
| `urls.py`       | Maps URLs to their respective views               |
| `admin.py`      | Configures the Django admin interface             |

#### **Configuration**
- **Settings Module**: Located in the TaskKing directory, it contains all necessary configurations, including installed apps, middleware, and static files settings.
- **Database**: SQLite (`db.sqlite3`) is used for development; it can be replaced with PostgreSQL or MySQL for production.
- **Static File Handling**: Configured with **WhiteNoise** for serving static files efficiently.

---

## **Project Organization**
- **Main App**: `todolist`
  - Follows Django's **MVT (Model-View-Template)** pattern.
  - Includes a dedicated `migrations` directory for database schema changes.
  - Separate directories for static assets and templates.
  - Python cache management with `__pycache__` for faster execution.

---

## **Deployment Setup**
- **`Procfile`**: Specifies commands for deploying the project on Heroku.
- **`requirements.txt`**: Lists project dependencies, including Django, WhiteNoise, and other required libraries.
- **`README.md`**: Comprehensive documentation for developers and users.

---

## **Design Elements**

### **Color Palette**
| **Element**         | **Color**           | **Hex Code**  |
|---------------------|---------------------|---------------|
| Background Gradient | Deep Purple → Cyan  | #4A0E4E → #00FFFF |
| Button Primary      | Coral Pink          | #FF6B6B       |
| Button Hover        | Light Coral         | #FF8787       |

### **Design Features**
- **Background**:  
  A dynamic 135-degree linear gradient from deep purple (#4A0E4E) to cyan (#00FFFF), providing a vibrant and modern look.
- **Cards**:  
  Semi-transparent white cards with a 10% opacity and subtle blur effect for a glassmorphism style.

### **Typography**
| **Text Element**  | **Font**     | **Weight** |
|-------------------|--------------|------------|
| Headers           | Poppins      | 600        |
| Body Text         | Roboto       | Normal     |

---

### **Interactive Elements**
- **Buttons**:
  - **Default State**: Coral Pink (#FF6B6B)
  - **Hover State**: Light Coral (#FF8787)
  - Smooth transitions and hover animations for a modern feel.
- **Task Items**:
  - Animated hover effect with a 5px upward movement and shadow effect.
  - Smooth 0.3s transition effects for all interactive elements.

---

## **Visual Overview**

### Color Palette
![TaskKing Color Palette](image)

### Interface Design
![TaskKing UI Design](image)

---

## **Future Enhancements**
- **User Profile Management**:  
  Allow users to edit profiles, upload avatars, and manage personal preferences.
- **Notifications**:  
  Implement email and in-app notifications for task deadlines and updates.
- **Task Sharing**:  
  Enable users to share tasks with team members and collaborate on task lists.
- **Advanced Analytics**:  
  Provide task completion rates, time tracking, and productivity insights.
- **API Integration**:  
  Expose REST APIs for external integrations with other task management tools or mobile apps.

---

## **Conclusion**
TaskKing is a scalable, user-friendly task management application built on Django. It combines modern UI/UX design with robust backend functionality, making it an ideal solution for both personal and team-based task management. The project adheres to Django best practices, ensuring maintainability, flexibility, and a smooth user experience across various devices and platforms.

