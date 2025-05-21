from web_scraper.scraper import get_all_products
from web_scraper.detail_scraper import scrape_product_details
from db.database import get_connection, create_table, save_products

def main():
    conn = get_connection()
    create_table(conn)

    products = get_all_products()

    for product in products:
        specs = scrape_product_details(product['Link'])
        product.update(specs)
        save_products(conn, product)
    
    conn.close()

if __name__ == "__main__":
    main()