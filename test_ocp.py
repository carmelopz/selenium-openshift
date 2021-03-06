from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_selenium():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    profile.set_preference('dom.webnotifications.enabled', False)

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
    
def test_remote_f():
    capabilities = DesiredCapabilities.FIREFOX.copy()
    #capabilities['marionette'] = True
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("https://poc.timwork.it")
    #driver.save_screenshot('screenshot.png')
    assert "Login" in driver.title

    assert True
    driver.quit() 
    
def test_remote_c():
    capabilities = DesiredCapabilities.CHROME.copy()
    #capabilities['binary'] = "/opt/google/chrome/chrome"
    #capabilities['marionette'] = False
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "65"

    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.quit()

def test_remote():
    # profile = webdriver.FirefoxProfile()
    # profile.accept_untrusted_certs = True
    # profile.set_preference('dom.webnotifications.enabled', False)

    capabilities = DesiredCapabilities.CHROME
    #capabilities['binary'] = "/opt/google/chrome/chrome"
    #capabilities['marionette'] = False
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "65"

    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()
    

    
def test_remote1():
    # profile = webdriver.FirefoxProfile()
    # profile.accept_untrusted_certs = True
    # profile.set_preference('dom.webnotifications.enabled', False)

    capabilities = DesiredCapabilities.FIREFOX
    capabilities['marionette'] = True
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()    
    
def test_remote2():
    # profile = webdriver.FirefoxProfile()
    # profile.accept_untrusted_certs = True
    # profile.set_preference('dom.webnotifications.enabled', False)

    capabilities = DesiredCapabilities.CHROME
    capabilities['marionette'] = False
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(command_executor='http://156.54.176.85:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()
   
    
def test_remote3():
    # profile = webdriver.FirefoxProfile()
    # profile.accept_untrusted_certs = True
    # profile.set_preference('dom.webnotifications.enabled', False)

    capabilities = DesiredCapabilities.FIREFOX
    capabilities['marionette'] = True
    #capabilities['platform'] = "WINDOWS"
    #capabilities['version'] = "7"

    driver = webdriver.Remote(command_executor='http://156.54.176.85:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

    assert True
    driver.close()
