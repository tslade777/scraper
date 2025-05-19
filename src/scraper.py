import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.bowlersmart.com/shop/bowling-gear/bowling-balls/page/{}/"
headers = {"User-Agent": "Mozilla/5.0"}

data = []
page = 1

while True:
    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    if "No products were found" in response.text or response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all('div', class_='type-product')

    if not products:
        break

    for product in products:
        link_tag = product.find("a", href=True)
        link = link_tag["href"] if link_tag else "No link"
        
        title_tag = product.select_one(".woocommerce-loop-product__title a, .woocommerce-loop-product__title")
        title = title_tag.get_text(strip=True) if title_tag else "No title"


        image_tag = product.find("img")
        image_url = image_tag["src"] if image_tag and image_tag.has_attr("src") else "No image"

        original_price_tag = product.find("del")
        original_price = original_price_tag.text.strip() if original_price_tag else "No original price"

        discounted_price_tag = product.find("ins")
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else "No discount"

        data.append({
            "Title": title,
            "Link": link,
            "Image URL": image_url,
            "Original Price": original_price,
            "Discounted Price": discounted_price
        })

    print(f"Scraped page {page}")
    page += 1

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("bowling_balls.csv", index=False)
print("✅ Saved to bowling_balls.csv")
