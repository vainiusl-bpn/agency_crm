# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Agency CRM system built with Flask for managing client relationships, brands, teams, and media commitments in a media agency context. The application follows a modular blueprint architecture with SQLAlchemy ORM for database operations.

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment variables (if .env.example exists)
cp .env.example .env
# Edit .env with your SECRET_KEY and other settings
```

### Running the Application
```bash
# Start development server (debug mode enabled)
python run.py
# Access at http://localhost:5000
```

### Database Operations
```bash
# Initialize migrations (first time only)
flask db init

# Create new migration after model changes
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Access Flask shell with pre-loaded models
flask shell
```

### Database Maintenance Scripts
When updating database schema, use the appropriate update script:
```bash
python update_database.py  # General updates
python update_planning_info.py  # Planning info updates
python create_recurring_tasks.py  # Recurring tasks setup
python create_subbrand_table.py  # Add subbrands functionality
```

## Architecture Overview

### Blueprint Structure
- **`auth/`**: Authentication (login, registration, password management)
- **`clients/`**: Core CRM functionality (companies, brands, contacts, agreements)
- **`team/`**: Team member management and assignments
- **`dashboard/`**: Main dashboard and reporting views

### Key Models (models.py)
- **User**: Team members with roles (Management, Project Manager, Account Manager, etc.)
- **Company**: Client companies with VAT, banking details, and subcompany relationships
- **Brand**: Multiple brands per company with team assignments
- **Subbrand**: Simple display-only subbrands for organizational purposes
- **ClientContact**: Individual contacts with birthday tracking for gift management
- **Agreement**: Document management for contracts
- **MediaGroup/Commitment**: Media spending tracking by channel and year
- **StatusUpdate**: Brand health monitoring (Perfect/Medium/Risk states)
- **PlanningInfo**: Campaign planning with KPIs and documentation
- **BrandTask**: Recurring tasks assigned to brands with completion tracking

### Important Relationships
- Companies can have multiple brands and subcompanies
- Brands can have multiple subbrands (display-only)
- Brands are assigned team members with one key person
- Each brand can have multiple status updates, planning info, and tasks
- Media commitments are tracked at the company level by year and media group
- Contacts can be associated with multiple brands

### File Upload Configuration
- Allowed extensions: PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, PNG, JPG, JPEG, GIF
- Upload folder: `app/static/uploads/`
- File size limit: 16MB (configured in Flask)

### Authentication & Security
- Flask-Login for session management
- Password hashing with Werkzeug
- CSRF protection via Flask-WTF
- File upload validation and sanitization

## Development Notes

### Database Schema Changes
Always use Flask-Migrate for schema changes:
1. Modify models in `models.py`
2. Generate migration: `flask db migrate -m "description"`
3. Review generated migration in `migrations/versions/`
4. Apply with `flask db upgrade`

### Adding New Features
1. Create new blueprint in appropriate module or new module
2. Register blueprint in `__init__.py`
3. Add models to `models.py` if needed
4. Create forms in module's `forms.py`
5. Add templates following existing structure

### Template Structure
- Base template: `templates/base.html`
- Uses Tailwind CSS for styling
- Flash messages automatically displayed
- Navigation menu in header for authenticated users
- JavaScript enhancements for filtering and searching

### Recent Feature Additions
- **Subbrands**: Brands can have multiple subbrands for display purposes
- **Excel Export**: Export functionality for brands, contacts, and companies
- **Advanced Filtering**: Client-side filtering on brands list page
- **Contact Assignment**: Improved workflow for assigning contacts to brands

### Testing Considerations
- Manual testing is currently used
- Test database operations with Flask shell
- Verify file uploads work correctly
- Check form validations and CSRF protection
- Test filtering and export functionality

### Common Issues and Solutions
- **Migration errors**: Check if running in correct virtual environment
- **File upload issues**: Ensure upload directory exists and has write permissions
- **CSRF token errors**: Make sure forms include `{{ form.hidden_tag() }}` or proper CSRF token
- **Database locked**: Close any open Flask shell sessions