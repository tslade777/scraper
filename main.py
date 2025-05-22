from web_scraper.scraper import get_all_products
from web_scraper.detail_scraper import scrape_product_details
from web_scraper.save import save_bowling_ball

def main():
    products = get_all_products()

    for product in products:
        specs = scrape_product_details(product['link'])
        print(specs)
        product.update(specs)
        save_bowling_ball(product)
        

if __name__ == "__main__":
    main()