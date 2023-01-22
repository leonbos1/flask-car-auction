from selenium import webdriver
from time import sleep
import requests
import sqlite3
import datetime

from car import Car
from requests import get

AUTOSCOUT_URL = "https://www.autoscout24.com/"
SYNC = True


def main():
    driver = webdriver.Chrome()
    cars = []

    driver.get(AUTOSCOUT_URL)
    sleep(0.5)

    accept_cookies(driver)

    sleep(0.5)

    scrape_home_page(driver, cars)

    if SYNC:
        save_cars_to_db(cars)
    else:
        for car in cars:
            print(car)


def scrape_home_page(driver: webdriver, cars: list):
    skip = 0
    while True:
        scrape_most_wanted(driver, cars=cars, cars_to_skip=skip)
        sleep(0.5)
        try:
            click_more_vehicles(driver)
        except:
            # when no more vehicles are available, break the loop
            break
        skip += 4


def scrape_most_wanted(driver: webdriver, cars: list, cars_to_skip: int):
    most_wanted = driver.find_elements_by_class_name(
        "listing-impressions-tracking")

    for i in most_wanted:
        # make sure we don't scrape the same car twice (or more)
        if cars_to_skip > 0:
            cars_to_skip -= 1
            continue

        card_summary = i.find_element_by_class_name("hf-listing-card__summary")
        location = card_summary.find_elements_by_tag_name("p")[-1].text

        image_div = i.find_element_by_class_name("hf-listing-card__image")
        image = image_div.find_element_by_tag_name("img").get_attribute("src")

        request = requests.get(image)
        image = request.content

        car = Car(guid=i.get_attribute("data-guid"), brand=i.get_attribute("data-make"), model=i.get_attribute("data-model"), price=i.get_attribute("data-price"), mileage=i.get_attribute(
            "data-mileage"), first_registration=convert_to_year(i.get_attribute("data-first-registration")), vehicle_type=i.get_attribute("data-vehicle-type"), location=location, image=image, condition=get_condition(int(i.get_attribute("data-mileage"))))

        cars.append(car)


def click_more_vehicles(driver: webdriver):
    more_vehicles_button = driver.find_element_by_xpath(
        "//button[contains(text(), 'More vehicles')]")
    more_vehicles_button.click()


def accept_cookies(driver: webdriver):
    cookies_button = driver.find_element_by_xpath(
        "//button[contains(text(), 'Accept')]")
    cookies_button.click()


def convert_to_year(first_registration: str):
    if first_registration.lower() == "new":
        return 2023
    else:
        return int(first_registration.split("-")[1])


def get_condition(mileage: int):
    if mileage < 10000:
        return "New"
    elif mileage < 150000:
        return "Used"
    else:
        return "Old"


def save_cars_to_db(cars: list):
    conn = sqlite3.connect("../instance/auctions.db")
    c = conn.cursor()

    for car in cars:
        c.execute("INSERT INTO car (guid, brand, model,year,condition,mileage) VALUES (?, ?, ?, ?, ?, ?)",
                  (car.guid, car.brand, car.model, car.first_registration, car.condition, car.mileage))
        conn.commit()
        print(f"Added {car.brand} {car.model} to database")

    for car in cars:
        car_id = c.execute("SELECT id FROM car WHERE guid = ?",
                           (car.guid,)).fetchone()[0]
        c.execute("INSERT INTO images (car_id, image) VALUES (?, ?)",
                  (car_id, car.image))
        conn.commit()
        print(f"Added image for {car.brand} {car.model} to database")

    for car in cars:
        car_id = c.execute("SELECT id FROM car WHERE guid = ?",
                           (car.guid,)).fetchone()[0]
        end_date = datetime.datetime.now() + datetime.timedelta(days=1)
        end_time = datetime.datetime.now() + datetime.timedelta(hours=1)
        end_date = end_date.strftime("%Y-%m-%d")
        end_time = end_time.strftime("%H:%M")

        latitude, longitude = get_latitude_longitude(car.location)

        c.execute("INSERT INTO auction (car_id, price, end_date, end_time, location, longitute, latitude, status, amount_of_bids) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (car_id, car.price, end_date, end_time, car.location, longitude, latitude, "pending", 0))
        conn.commit()
        print(f"Added auction for {car.brand} {car.model} to database")


def get_latitude_longitude(location: str):

    url = f"https://geocode.maps.co/search?q={location}"
    response = get(url)
    json = response.json()

    latitude = json[0]["lat"]
    longitude = json[0]["lon"]

    return latitude, longitude


if __name__ == "__main__":
    main()
