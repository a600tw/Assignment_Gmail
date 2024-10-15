from selenium.webdriver.common.by import By

class GmailPagesObject():

    COMPOSE_BTN = (By.XPATH, "//html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div")
    
    INPUT_TO = (By.CSS_SELECTOR, "input[aria-label=\"To recipients\"]")
    # INPUT_TO = (By.CSS_SELECTOR, "/hdiv[2]/table/tbody/table/tbody/tr[1]/iv/input")

    
    

    INPUT_SUBJECT = (By.NAME, 'subjectbox')
    INPUT_BODY = (By.CSS_SELECTOR, '.Am.Al.editable.LW-avf.tS-tW')
    SEND_BTN = (By.XPATH, "//div[text()='Send']")

    

 
    OPTION_BTN = (By.XPATH, "//div[@aria-label='More options']")
    OPTION_BTN_INMAIL = (By.XPATH, "//div[@aria-label='More email options']")

    
    
    LABEL_SELECTOR = (By.XPATH ,"//span[@class='J-Ph-hFsbo']")
    # LABEL_BTN = (By.XPATH, '//*[@id=":vm"]')
    SOCIAL_SELECTOR = (By.XPATH, "//div[@class='J-LC-Jz' and text()='Social']/div[@class='J-LC-Jo J-J5-Ji']")
    # SOCIAL_SELECTOR = (By.XPATH, "/html/body/div[38]/div/div[3]/div[1]/div/div")
    SOCIAL_APPLY = (By.XPATH, "//div[contains(text(),'Apply')]")


    # SEARCH_MAIL_BAR = (By.XPATH, "//input[@placeholder='Search mail']")
    SEARCH_MAIL_BAR = (By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/div/div[2]/div[2]/header/div[2]/div[2]/div[2]/form/div/table/tbody/tr/td/table/tbody/tr/td/div/input[1]")
    
    FIRST_MAIL = (By.XPATH, "//table[@role='grid']//tr[1]")

    STAR_MAIL = (By.XPATH, "//span[@aria-label='Not starred']")
    # STAR_MAIL = (By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[6]/div[1]/div/table/tbody/tr/td[3]/span")
    

    MAIL_SUBJECT = (By.XPATH, "//*[@id=':1']/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/h2")
    MAIL_BODY = (By.XPATH, "//div[@dir='ltr' and normalize-space(text())='PB Test WOW']")


    SOCIAL_STATUS = (By.XPATH, "//div[@title='Social' and @aria-checked='true']")
    

    DELETE_MAIL = (By.CSS_SELECTOR, "div[class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA'] div[class='asa']")

    INBOX_BTN = (By.XPATH, "//a[normalize-space()='Inbox']")
    