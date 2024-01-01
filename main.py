import os
import csv
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def main():
    chrome_options = ChromeOptions()
    driver = Chrome(options=chrome_options)

    wait_for_user_login(driver)
    wait_for_region_selection(driver)

    dataset = get_city_district_town_dataset(driver)

    save_to_csv(dataset)

    input("Press Enter to close the browser...")
    driver.quit()


def get_city_district_town_dataset(driver):
    cities_element = driver.find_element(By.ID, "cityId")
    dataset = []

    select = Select(cities_element)

    for city_option in select.options[1:]:
        city_name = city_option.text
        print(f"Selecting city: {city_name}")

        city_option.click()

        district_id_hidden = is_element_hidden(driver, "districtId")
        town_id_hidden = is_element_hidden(driver, "townId")

        if district_id_hidden and not town_id_hidden:
            # Case: districtId is hidden, townId is visible
            towns = get_town(driver)
            dataset.extend([(city_name, "", town) for town in towns])

        elif not district_id_hidden:
            # Case: districtId is visible
            districts_with_towns = get_district_town(driver)
            dataset.extend(
                [(city_name, district, town) for district, town in districts_with_towns]
            )

        else:
            # Case: Both districtId and townId are hidden
            dataset.append((city_name, "", ""))

    return dataset


def get_district_town(driver):
    district_select_element = driver.find_element(By.ID, "districtId")
    district_select = Select(district_select_element)
    districts_with_towns = []

    for district_option in district_select.options[1:]:
        district_name = district_option.text
        print(f"Selecting district: {district_name}")

        district_option.click()

        towns = get_town(driver)
        districts_with_towns.extend((district_name, town) for town in towns)

    return districts_with_towns


def get_town(driver):
    town_select_element = driver.find_element(By.ID, "townId")
    town_select = Select(town_select_element)
    towns = [town_option.text for town_option in town_select.options[1:]]
    return towns


def wait_for_user_login(driver):
    url = f"https://www.mubawab.ma/"
    print("Loading website:", url)
    driver.get(url)
    WebDriverWait(driver, 100).until(EC.url_contains(url))

    close_button = driver.find_element(By.CSS_SELECTOR, "div.fancybox-close")
    close_button.click()

    post_button = driver.find_element(By.CSS_SELECTOR, "a.float-left.btn-head")
    post_button.click()


def wait_for_region_selection(driver):
    print("Waiting for user to select preffered language and region.")
    WebDriverWait(driver, 100).until(
        lambda driver: driver.execute_script(
            "return document.getElementById('regionId').selectedIndex !== 0"
        )
    )


def is_element_hidden(driver, element_id):
    element = driver.find_element(By.ID, element_id)
    print(element_id, element.is_displayed())
    return not element.is_displayed()


def save_to_csv(data):
    csv_file_path = "output.csv"

    # Check if the file already exists
    count = 0
    while os.path.exists(csv_file_path):
        count += 1
        csv_file_path = f"output ({count}).csv"

    with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["City", "District", "Town"])
        writer.writerows(data)

    print(f"Data saved to: {os.path.abspath(csv_file_path)}")


if __name__ == "__main__":
    main()
