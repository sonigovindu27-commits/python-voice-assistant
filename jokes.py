
import requests

def joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    json_data = requests.get(url).json()

    arr = ["", ""]
    arr[0] = json_data["setup"]
    arr[1] = json_data["punchline"]

    return arr


#if __name__ == "__main__":
   # j=joke()
   # print(j[0])
  #  print(j[1])
