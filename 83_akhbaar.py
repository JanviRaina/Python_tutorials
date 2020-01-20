#first install :-     pip install pywin32
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=="__main__":
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=7b62007d07f742eb80a14c03bc69c172')
    response=requests.get(url)
    data=response.text
    parsed=json.loads(data)
    for i in range(0,10):
        speak(parsed['articles'][i]['title'])
