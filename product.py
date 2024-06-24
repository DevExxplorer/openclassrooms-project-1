def get_number_star(data):
    match data['class'][1]:
        case "One":
            result = 1
        case "Two":
            result = 2
        case "Three":
            result = 3
        case "Four":
            result = 4
        case "Five":
            result = 5
        case _:
            result = "Error"

    return result


def get_info_product(data):
    product = {
        "title": data.h1.string,
        "price": data.find(class_="price_color").string,
        "star_rating": get_number_star(data.find(class_="star-rating")),
        "description": data.find(id="product_description").find_next_sibling().string,
        "upc": data.find_all('td')[0].string,
        "product_type": data.find_all('td')[1].string,
        "price_excl_tax": data.find_all('td')[2].string,
        "price_incl_tax": data.find_all('td')[3].string,
        "tax": data.find_all('td')[4].string,
        "availability": data.find_all('td')[5].string,
        "number_reviews": data.find_all('td')[6].string,
    }

    return product
