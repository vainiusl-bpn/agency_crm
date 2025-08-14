# Agency Customer Success Management System

A professional CRM system built for media agencies to manage client relationships, brands, teams, and campaigns.

## 🆕 Recent Updates

### New Features Added:
- **Enhanced Contact Management**: Contact type categorization (Client/Partner/Media) with advanced filtering
- **Media Planning Module**: Comprehensive quarterly budget planning with variance tracking
- **Digital Information Hub**: Centralized digital asset management with 4 specialized sections
- **Interactive Brand Sorting**: Click-to-sort functionality for improved brand management
- **URL Auto-Formatting**: Automatic https:// addition for external links
- **Improved Database Relationships**: Better cascade delete handling for data integrity

## Features

### Core CRM Features
- **Team Management**: Manage agency team members with different roles (Management, Project Manager, Campaign Manager, ATL Planner, Digital Trafficer, etc.)
- **Client Companies**: Store company information including VAT code, address, bank account details
- **Document Management**: Upload and manage agreements (PDF files)
- **Brand Management**: Manage multiple brands per company with subbrands
- **Team Assignment**: Assign team members to brands with key responsible person designation
- **Planning Information**: Add planning comments and KPIs for brands
- **Commitments**: Track yearly media commitments by company and media group
- **Status Updates**: Monitor brand health with status evaluations (Perfect/Medium/Risk)
- **Dashboard**: Overview of all activities and risk indicators

### Enhanced Contact Management
- **Contact Types**: Categorize contacts as Client, Partner (Agency/Creative), or Media Channel
- **Contact Filtering**: Filter contacts by type, brand, company, or search terms
- **Gift & Newsletter Management**: Track gift preferences and newsletter subscriptions
- **Birthday Tracking**: Monitor contact birthdays for gift planning

### Media Planning & Budget Management
- **Quarterly Planning**: Plan media budgets by year and quarter (Q1-Q4)
- **Multi-Channel Support**: Track different media types (TV, Radio, Digital, OOH, Print)
- **Budget vs Actual**: Compare planned budgets with actual spend
- **Variance Reporting**: Automatic variance calculation with percentage tracking
- **Channel Management**: Organize campaigns by specific channels/platforms

### Digital Information Hub
- **Digital Planning Info**: Store terminology, KPIs, campaign types, portal agreements
- **Digital AdOps Info**: Account details, permissions, ad page specifications
- **Digital Tracking Info**: Tracking event descriptions and naming conventions across systems (GA4, Meta, Google Ads)
- **Digital Resource Links**: Categorized links to ad accounts, dashboards, reports, creative requirements
- **Auto URL Formatting**: Automatic https:// addition for external links

### Advanced Brand Management
- **Interactive Sorting**: Click-to-sort brands by name, key person, risk level, last update, or status
- **Visual Risk Indicators**: Color-coded status badges (Perfect/Medium/Risk)
- **Key Person Assignment**: Track responsible team members for each brand
- **Comprehensive Brand Views**: Unified access to planning, media, and digital information

## Installation

1. Clone the repository:
```bash
cd agency_crm
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

5. Access the application at `http://localhost:5000`

## First Time Setup

1. Register a new user account
2. Login with your credentials
3. Start by creating Media Groups (Admin > Media Groups)
4. Add your first company
5. Create brands for the company
6. Add client contacts
7. Assign team members to brands

## Database Schema

The system uses SQLite with the following main entities:

### Core Entities
- **Users**: Team members with roles and permissions
- **Companies**: Client companies with subcompany relationships
- **Brands**: Multiple brands per company with subbrands
- **Client Contacts**: Enhanced with contact types (client/partner/media)
- **Agreements**: Document management for contracts

### Media & Planning
- **Media Groups**: Channel categorization
- **Commitments**: Yearly media spending commitments
- **Media Plans**: Quarterly budget planning by channel and media type
- **Planning Information**: Campaign planning and KPIs
- **Status Updates**: Brand health monitoring

### Digital Information
- **Digital Info**: Comprehensive digital information storage (planning, AdOps, tracking)
- **Digital Info Links**: Categorized external resource links

### Task & Project Management
- **Task Templates**: Recurring task definitions
- **Brand Tasks**: Brand-specific recurring tasks
- **Task Completions**: Task execution tracking
- **Invoices**: Financial tracking and billing

## Security

- User authentication with password hashing
- Session management
- File upload restrictions (PDF only)
- Form validation and CSRF protection

## Technologies

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Tailwind CSS
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **File Uploads**: Werkzeug