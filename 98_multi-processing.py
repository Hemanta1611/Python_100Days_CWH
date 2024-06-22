import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    with open(f"FILE98/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    # downloadFile(url, i)
    url = "https://picsum.photos/2000/3000"
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()



