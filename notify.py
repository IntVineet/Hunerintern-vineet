'''# installing the requests package  
$ pip install requests  
# installing the plyer package  
$ pip install plyer''' 






from plyer import notification  
  
notification_title = 'Hello HunerIntern!'  
notification_message = 'Thank you For giving me this brillient task.'  
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  
