from requests import get

def get_latitude_longitude(location: str):

    url = f"https://geocode.maps.co/search?q={location}"
    response = get(url)
    json = response.json()

    latitude = json[0]["lat"]
    longitude = json[0]["lon"]

    return latitude, longitude