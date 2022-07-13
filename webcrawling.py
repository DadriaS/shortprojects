"""Currently, users enter some data on an online platform. The aim is to develop a database and automate the update. This does not run entirely. 
There is a hover over button that is giving me a problem to be clicked (line 30). Te button is also with in an iframe (line 27). 
I have tried a few packages. When I complete it, I'll update this file."""

from playwright.sync_api import sync_playwright
  
username = username
password = password
url=site

with sync_playwright() as p:
   
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = browser.new_page()
    page.goto(url)
    #find username and password and enter
    page.fill('#name', username)
    page.fill('#password', password)
    page.click('button:text("Log into Account")')
    #navigate to plants
    page.locator("button", has_text="Cultivation").click()
    page.locator(".glyphicon.glyphicon-stats[width='50px']").click()
    with page.expect_event("popup") as page_info: #new tab
        page.evaluate("window.open('https://app.mjplatform.com/reporting/analytics/view/16')")
        popup = page_info.value
    
    frame = popup.frame('frame-domo_report_embed') #frame
    popup.screenshot(path="python.png")
    print("frame found")
    frame.hover('#pg-layout-content > div > div > div > div > div > div > span:nth-child(22) > pg-layout-frame > cmpl9fqbbgud0 > div > div > pg-layout-populated-frame > cmpk5kob4hlxk > div > div.pg-layout-populated-frame > section > cd-control-menu > div > button > i')
    export_button=popup.frame('frame-domo_report_embed').locator('#pg-layout-content > div > div > div > div > div > div > span:nth-child(22) > pg-layout-frame > cmpl9fqbbgud0 > div > div > pg-layout-populated-frame > cmpk5kob4hlxk > div > div.pg-layout-populated-frame > section > cd-control-menu > div > button > i')
    
    
    
    with popup.expect_download() as download_info:
        export_button.click()
    download = download_info.value
    #export_button.click()

    print("Frame found")  


    #download plant information
        
    popup.screenshot(path="python.png")
    browser.close()    
