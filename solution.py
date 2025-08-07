import pandas
import re 


def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    is_valid_label = lambda label: re.match(r"^[a-zA-Z_]+$", label) is not None

    if not is_valid_label(new_column):
        return pandas.DataFrame([])

    for col in df.columns:
        if not is_valid_label(col):
            return pandas.DataFrame([])

  
    role_cleaned = role.strip()
    operator = None
    supported_operators = ["+", "-", "*"]

    for op in supported_operators:
        if op in role_cleaned:
            operator = op
            break

    if operator is None: 
        return pandas.DataFrame([])

    parts = [p.strip() for p in role_cleaned.split(operator)]
    if len(parts) != 2:
        return pandas.DataFrame([])

    col1_name, col2_name = parts


    if not is_valid_label(col1_name) or not is_valid_label(col2_name):
        return pandas.DataFrame([]) 

    if col1_name not in df.columns or col2_name not in df.columns:
        return pandas.DataFrame([]) 

    df_result = df.copy()
    if operator == "+":
        df_result[new_column] = df_result[col1_name] + df_result[col2_name]
    elif operator == "-":
        df_result[new_column] = df_result[col1_name] - df_result[col2_name]
    elif operator == "*":
        df_result[new_column] = df_result[col1_name] * df_result[col2_name]

    return df_result