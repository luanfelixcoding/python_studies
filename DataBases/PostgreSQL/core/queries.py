import psycopg2


def execute_query(conn, query: str, params=None, fetch: bool = False):
    """
    Executes a SQL query and returns the results if necessary.
    """
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            else:
                conn.commit()
                return cur.rowcount()
    except psycopg2.Error as unknown_error:
        print(f"Error in executing query: {unknown_error}")
        conn.rollback()  # Rollback the transaction in case of error
        return None


def create_product(conn, name: str, description: str, price: float, stock_quantity: int, category_id: int = None):
    """
    Insert a new product on products table.

    Args:
        name (str) : name of the product
        description (str) : description of the product
        price (float) : price of the product
        stock_quantity (int) : quantity of the product in stock
        category_id (int) = None : Id category of the product
    """
    query = """
    INSERT INTO products(name, description, price, stock_quantity, category_id)
    VALUES (%s, %s, %s, %s, %s) RETURNING product_id;
    """

    result = execute_query(
        conn, (name, description, price, stock_quantity, category_id), fetch=True)
    return result[0][0] if result else None


def get_product_by_id(conn, product_id: int):
    """
    Search a product by its id.
    """
    query = "SELECT * from products WHERE product_id = %s;"
    return execute_query(conn, query, (product_id,), fetch=True)


def get_all_products(conn):
    """
    Search for all products in products table.
    """
    query = "SELECT p.*, c.name as category_name FROM products p LEFT JOIN categories c ON p.category_id = c.category_id;"
    return execute_query(conn, query, fetch=True)


def update_product_stock(conn, product_id: int, new_stock: int):
    """
    Update the stock quantity of a product.
    """
    query = "UPDATE products SET stock_quantity = %s WHERE product_id = %s;"
    return execute_query(conn, query, (new_stock, product_id))


def delete_product(conn, product_id: int):
    """
    Delete a product by ID.
    """
    query = "DELETE FROM products WHERE product_id = %s;"
    return execute_query(conn, query, (product_id,))


def create_category(conn, name: str):
    """
    Insert a new category in the categories table.
    """
    query = """
    INSERT INTO categories (name) VALUES (%s) RETURNING category_id;
    """
    result = execute_query(conn, query, (name,), fetch=True)
    return result[0][0] if result else None


def get_all_categories(conn):
    """
    Search for all categories in categories table.
    """
    query = "SELECT * FROM categories;"
    return execute_query(conn, query, fetch=True)
