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
        "coverstock": "coverstock",
        "coverstock name": "coverstock_name",
        "core": "core",
        "core name": "core_name",
        "scent": "scent",
        "rg": "rg",
        "differential": "diff",
        "mass bias": "mass_bias",
        "brand": "brand",
        "release date": "release_date",
        "color": "color",
        "finish": "finish",
        "flare": "flare"
    }


    for spec in specs: 
        th = spec.select_one("th")
        td = spec.select_one("td")

        if not th or not td:
            continue

        raw_label = th.get_text(strip=True)
        value = td.get_text(strip=True)

        normalized_label = normalize_label(raw_label)

        field = label_map.get(normalized_label)

        if field:
            item[field] = value
        else:
            print(f"⚠️ Unmatched label: {raw_label} → {normalized_label}")
    
    return item

def normalize_label(label: str) -> str:
    label_lower = label.lower()
    result = ""
    if "core name" in label_lower:
        result = "core name"
    elif "core type" in label_lower or "core shape" in label_lower:
        result = "core"
    elif "cover name" in label_lower:
        result = "coverstock name"
    elif "coverstock type" in label_lower:
        result = "coverstock"
    elif "mass bias" in label_lower:
        result = "mass bias"
    elif "radius of gyration" in label_lower:
        result = "rg"
    elif "differential" in label_lower:
        result = "differential"
    elif "color" in label_lower:
        result = "color"
    elif "brand" in label_lower:
        result = "brand"
    elif "scent" in label_lower:
        result = "scent"
    elif "surface finish" in label_lower:
        result = "finish"
    elif "flare potential" in label_lower:
        result = "flare"
    elif "release date" in label_lower:
        result = "release date"
    return result
