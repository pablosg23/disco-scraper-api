from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import json
import sqlite3

with open("datos.json", "w") as f:
    dict1 = {"records":[]}
    json.dump(dict1, f)

def write_json(new_data, filename='datos.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["records"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def scraper(categoria='electro/informatica'):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)

    site = f'https://www.disco.com.ar/{categoria}'

    driver.get(site)

    wait = WebDriverWait(driver, 10)
    while True:
        try:
            button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Mostrar más')]")))
            driver.execute_script("arguments[0].click();", button)
            try:
                total_height = int(driver.execute_script("return document.body.scrollHeight"))

                for i in range(1, total_height, 1000):
                    driver.execute_script("window.scrollTo(0, {});".format(i))
            except:
                pass
        except NoSuchElementException:
            break
        except TimeoutException:
            break
        except StaleElementReferenceException:
            break
    try:
        lista_elementos = driver.find_element(By.XPATH, '//div[@id="gallery-layout-container"]')
        items = lista_elementos.text.split('\n')
        count_a = items.count('Agregar') #Cantidad de elementos
        for i in range(1, count_a+1):
            marca = lista_elementos.find_element(By.XPATH, f".//div[{i}]/section/a/article/div[3]/span").text
            descripcion = lista_elementos.find_element(By.XPATH, f".//div[{i}]/section/a/article/div[4]/h2/span").text
            precio = lista_elementos.find_element(By.XPATH, f".//div[{i}]/section/a/article//div[5]/div/div/div/div[1]/div/div/div[2]/div/span").text
            write_json({
                "id": i,
                "marca": marca.upper(),
                'descripcion': descripcion,
                'precio': precio
                })
    except:
        pass
    driver.quit()
    return 'Done'

def to_db():
    connection = sqlite3.connect('apidb.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM productos')
    connection.commit()
    connection.close()
    connection = sqlite3.connect('apidb.db')
    cursor = connection.cursor()
    datos = json.load(open('datos.json'))
    columns = ['id','marca','descripcion','precio']
    for row in datos["records"]:
        keys= tuple(row[c] for c in columns)
        cursor.execute('insert into productos values(?,?,?,?)',keys)
    connection.commit()
    connection.close()
    return 'Done'

if __name__ == '__main__':
    scraper(categoria='electro/informatica')