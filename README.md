📌 About The Project

**Virarkar Fashion** is a full-stack e-commerce web application developed using **Python and Django**.  
The project is designed to provide a complete online shopping experience where users can browse fashion products, add items to their cart, manage orders, and interact with products through reviews and wishlist features.

This project was developed to understand real-world web application development, including frontend design, backend logic, database management, authentication, and e-commerce workflows.


 🚀 Features

👤 User Features
- User registration and authentication
- Login and logout functionality
- Browse products by categories
- View detailed product information
- Product reviews and ratings
- Add products to wishlist
- Add products to cart
- Increase/decrease cart quantity
- Stock availability checking
- Checkout system
- Order history tracking
  
 🛒 E-Commerce Features
- Product management system
- Category-based product filtering
- Product search functionality
- Dynamic cart system
- Automatic order creation
- Stock validation before checkout
- Order status management

 🔐 Admin Features
- Manage products
- Add product categories
- Update product stock
- Manage customer orders
- Update order status
- Manage reviews

🛠️ Tech Stack

# Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

# Backend
- Python
- Django Framework

# Database
- SQLite

# Tools Used
- VS Code
- Git & GitHub

## Run in GitHub Codespaces / VS Code

This project is a **Django application**, so do not use the **Go Live** button or Live Server on port `5500`. Live Server is intended for static files and will display the repository directory instead of rendering Django templates.

Use the included VS Code task instead:

1. Open the repository in Codespaces.
2. Open **Terminal → Run Task**.
3. Select **Run Virarkar Fashion (Django)**.
4. Open the forwarded port named **Virarkar Fashion website** on port `8000`.

The equivalent terminal command is:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

Then open the forwarded URL shown in the **Ports** panel. The repository includes `.devcontainer/devcontainer.json`, which forwards port `8000` and opens the Django preview automatically, and `.vscode/tasks.json`, which provides the one-click launch task.
