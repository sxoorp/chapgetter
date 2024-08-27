import os
import requests

def downloader(url, chapter, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url + chapter)
    data = response.json()

    print(f"Found {len(data)} Page(s)")
    
    for item in data:
        img = item["img"]
        number = item["page"]
        filename = f"{number}.jpg"
        fpath = os.path.join(folder, filename)

        img_response = requests.get(img)
        
        with open(fpath, "wb") as file:
            file.write(img_response.content)
            print(f"Downloaded Page {number}")

    print("Done!")

def main():
    url = "https://consumet-public.vercel.app/manga/mangadex/read/"
    while True:
        chapter = input("Chapter ID ➜ ")
        if chapter.lower() == "quit":
            break
        folder = input("Output Folder ➜ ")
        downloader(url, chapter, folder)

if __name__ == "__main__":
    main()