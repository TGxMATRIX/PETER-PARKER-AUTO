import pyrogram
import requests
from bs4 import BeautifulSoup

def get_images(query):
  """Gets a list of images from Google Images for the given query."""
  url = "https://www.google.com/search?q=" + query
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  images = soup.find_all("img")
  return images

def download_image(image):
  """Downloads the given image from Google Images."""
  image_url = image["src"]
  response = requests.get(image_url)
  with open(image_url.split("/")[-1], "wb") as f:
    f.write(response.content)

  @bot.on_message()
  async def handle_message(message):
    if message.text == "/photo":
      query = message.text.split(" ")[1]
      images = get_images(query)
      for image in images:
        download_image(image)
        await bot.send_photo(message.chat.id, image)
