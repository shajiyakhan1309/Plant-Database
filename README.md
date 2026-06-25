# Plant-Database

A user-friendly desktop application for managing and storing comprehensive plant information. Built with Python and Tkinter, this application provides an intuitive graphical interface for cataloging plant data with scientific classification details.

## 🌿 Overview

Plant Database is a Python-based application that allows users to systematically record and manage information about various plant species. The application features a clean, organized form interface and uses SQLite for persistent data storage.

## ✨ Features

- **Comprehensive Plant Data Entry**: Record multiple attributes for each plant:
  - Basic Information (Plant Name, Plant ID)
  - Physical Characteristics (Plant Color, Fruit Color, Season)
  - Biological Classification (Kingdom, Order, Family, Genus)
  - Plant Benefits (Health, Beauty, Food, Medicine, Ornamental, Environmental, Aromatic, Culinary)
  - Description and Code Fields

- **User-Friendly GUI**: Clean, organized form interface built with Tkinter
- **Data Validation**: Ensures all required fields are completed before data submission
- **Persistent Storage**: SQLite database (`plants.db`) for reliable data persistence
- **Easy Data Management**: Form auto-clears after successful entry
- **Dropdown Menus**: Pre-populated options for common values to ensure data consistency

## 🛠️ Technical Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Database**: SQLite3
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 📋 Requirements

- Python 3.6 or higher
- Tkinter (typically bundled with Python)
- sqlite3 (standard library)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shajiyakhan1309/Plant-Database.git
   cd Plant-Database
   ```

2. Ensure Python 3.6+ is installed on your system

3. No additional dependencies required (Tkinter and sqlite3 are included with Python)

## 📖 Usage

Run the application:
```bash
python main.py
```

### How to Use:

1. **Fill in Plant Information**:
   - Enter the plant name and unique plant ID
   - Select the plant color and fruit color from the dropdown menus
   - Choose the season(s) when the fruit appears

2. **Add Classification Details**:
   - Select the kingdom (typically "Plantae")
   - Choose the order, family, and genus from predefined options
   - Enter a unique code for reference

3. **Specify Benefits**:
   - Select applicable benefits for the plant (Health, Food, Medicine, etc.)

4. **Add Description**:
   - Use the text area to add detailed information about the plant

5. **Submit Data**:
   - Click "Enter data" to save the plant information to the database
   - Success message will appear upon successful entry
   - Form will automatically clear for the next entry

## 🗄️ Database Schema

The application creates a SQLite table `plant_info` with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key, auto-incremented |
| plant_name | TEXT | Name of the plant |
| plant_id | TEXT | Unique plant identifier |
| plant_color | TEXT | Color of the plant |
| fruit_color | TEXT | Color of the fruit |
| fruit_season | TEXT | Season of fruit bearing |
| benefits | TEXT | Medicinal/dietary benefits |
| kingdom | TEXT | Biological kingdom |
| code | TEXT | Plant code/reference |
| plant_order | TEXT | Taxonomic order |
| family | TEXT | Plant family |
| genus | TEXT | Plant genus |
| description | TEXT | Detailed description |

## 📁 Project Structure

```
Plant-Database/
├── main.py          # Main application file
├── plants.db        # SQLite database (created after first run)
└── README.md        # This file
```

## 🎯 Future Enhancements

- Search and filter functionality for existing plant records
- Edit/update plant information
- Delete plant records
- Export data to CSV format
- Plant image upload capability
- Advanced botanical classification options
- Data backup and restore features

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues and bugs
- Suggest new features
- Improve documentation
- Submit pull requests

## 👤 Author

**Shajiya Khan**  
GitHub: [@shajiyakhan1309](https://github.com/shajiyakhan1309)

## 🙏 Acknowledgments

- Tkinter documentation and community
- SQLite for reliable database functionality
- Python for its simplicity and power

---

**Note**: The database file `plants.db` is automatically created when you first run the application. Make sure you have write permissions in the application directory.
