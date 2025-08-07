# Virtual Columns in Pandas

## Task Description

This project is a solution to a recruitment task that involves implementing the `add_virtual_column` function. The purpose of this function is to add a new virtual column to an existing DataFrame, where the values in the new column are calculated based on a simple mathematical operation (`+`, `-`, `*`) applied to two existing columns.

A key aspect of the task is robust validation of the input data. The function must return an empty DataFrame in cases where the column names are invalid or the calculation rule is incorrect.

## How to Run

### Requirements
* Python 3.8+
* pip

### Installation and Running Tests

1. **Clone the repository:**
    ```bash
    git clone https://github.com/(username)/Virtual-columns.git
    cd Virtual-columns
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run tests:**
    ```bash
    pytest
    ```