from time import sleep

from faker import Faker
from platinum import Chromium

from selenium import webdriver


def generate_account(mark='yeah'):
    faker = Faker()
    user = faker.name().replace(' ', mark)
    email = mark + faker.email()
    password = faker.password()
    return user, email, password


def auto_stars(*repos, headless=True):
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument(Chromium.HEADLESS)
    else:
        options.add_argument(Chromium.START_MAXIMIZED)
        options.add_argument(Chromium.DISABLE_INFOBARS)

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://github.com/join?source=header-home')

    user, email, password = generate_account()
    driver.find_element_by_id('user_login').send_keys(user)
    driver.find_element_by_id('user_email').send_keys(email)
    driver.find_element_by_id('user_password').send_keys(password)
    sleep(2)
    driver.find_element_by_id('signup_button').click()
    sleep(2)
    driver.find_element_by_xpath('//div[@class="SignUpContinueActions"]/button[@type="submit"]').click()
    sleep(2)
    driver.find_element_by_xpath('//form[@class="setup-form"]/input[@type="submit"]').click()
    sleep(2)

    for repo in repos:
        driver.get(repo)
        driver.find_element_by_xpath('//form[@class="unstarred js-social-form"]/button[@type="submit"]').click()
        print('Star {}'.format(repo))
        sleep(2)

    driver.quit()


if __name__ == '__main__':
    repos = ['https://github.com/fjwCode/cerium', 'https://github.com/fjwCode/auto-answer-tnwz', 'https://github.com/fjwCode/platinum', 'https://github.com/fjwCode/wireless-control']
    auto_stars(*repos)