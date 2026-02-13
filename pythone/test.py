import pyautogui
import time

def send_whatsapp_message(contact_name, message,delay=0.5,epoch=5):
    # Open WhatsApp Desktop Application
    
    pyautogui.press('win')          # Open Start Menu
    time.sleep(1)

    pyautogui.typewrite('whatsapp')      # App name
    time.sleep(0.5)
    pyautogui.press('enter')        # Launch app
    
    time.sleep(1)
    # go to search bar
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.typewrite(contact_name, interval=0.02)  # Type contact name
    time.sleep(1)  # Wait for search results to load
    pyautogui.press('enter')  # Select the contact
    pyautogui.sleep(0.5)  # Wait for chat to open
    
    # # Type and send the message

    pyautogui.sleep(2)  # Wait for chat to open
    for epoch in range(epoch):
        pyautogui.typewrite(message, interval=0.02)
        pyautogui.press('enter')  # Send the message
        time.sleep(delay)

send_whatsapp_message("twya", "i hate you soooooooooooo much 😘😘😘" ,delay=0.2,epoch=101)
    
