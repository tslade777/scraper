import requests
from bs4 import BeautifulSoup



def scrape_product_details(link):
    item = {}

    # Get product details
    detail_res = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    detail_soup = BeautifulSoup(detail_res.text, "html.parser")

    table = detail_soup.find("table", class_="woocommerce-product-attributes")
    specs = table.select("tr.woocommerce-product-attributes-item")

    label_map = {
        "Coverstock": "coverstock",
        "Core": "core",
        "Scent": "scent",
        "RG": "rg",
        "Differential": "diff",
        "Intermediate Differential": "mass_bias",
        "Brand": "brand",
        "Release Date": "release_date"
    }

    for spec in specs: 
        label = spec.select_one("th").get_text(strip=True)
        value = spec.select_one("td").get_text(strip=True)
        
        label_lower = label.lower()

        field = None
        for key, mapped_field in label_map.items():
            if key.lower() in label_lower:
                field = mapped_field
                break
        if field:
            item[field] = value
    
    return item