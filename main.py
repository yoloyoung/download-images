import os
import requests


def get_data():
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }

    img_list = []
    for i in range(304, 341):
        url = f"https://vshkole.com/8-klass/reshebniki/algebra/os-ister-2021/rozdil-1-ratsionalni-virazi/10-vlastivosti-stepenya-iz-tsilim-pokaznikom/{i}"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"{i}.png", "wb") as file:
            file.write(response)
            img_list.append(f"media\{i}.png")
            print(f"Downloaded {i} of 341")


def main():
    get_data()

if __name__ == '__main__':
    main()