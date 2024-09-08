"""
pip install httpx
# macOS
pip freeze | grep httpx >> requirements.txt
# Windows
pip freeze | findstr httpx >> requirements.txt

pip install -r requirements.txt

pwd: ดู working directory ปัจจุบัน
cd: เปลี่ยน directory (cd .. คือ ย้อนกลับขั้น) (cd <ชื่อ folder> คือ ไปเข้า folder นั้น)
ls: ดูไฟล์ใน folder ปัจจุบัน
which python: ดูที่อยู่ของ python ที่ใช้งานอยู่
"""
"""
poetry init
poetry add httpx
poetry add rich
"""
import httpx
import rich

# search_url = "https://api.thecatapi.com/v1/images/search?limit=1"
# search_response = httpx.get(search_url)
# search_data = search_response.json()
# cat_file_url = search_data[0]["url"]
# rich.print(cat_file_url)
# cat_file_response = httpx.get(cat_file_url)
# file_name = search_data[0]["url"].split("/")[-1]
# with open(file_name, "wb") as file:
#     file.write(cat_file_response.content)


def search_random_cat() -> str:
    """
    Search for a random cat image.
    Args:
        None
    Returns:
        str: URL of the cat image.
    """
    url = "https://api.thecatapi.com/v1/images/search?limit=1"
    r = httpx.get(url)
    r.raise_for_status()
    url = r.json()[0]["url"]
    
    return url


def get_file_name(url: str) -> str:
    """
    Get the file name from the URL.
    Args:
        url (str): URL of the file.
    Returns:
        str: File name.
    """
    return url.split("/")[-1]


def download_cat() -> str:
    """
    Download and write the image from the URL.
    Args:
        url (str): URL of the image.
    Returns:
        str: File name.
    """

    url = search_random_cat()
    file_name = get_file_name(url)
    r = httpx.get(url)

    with open(file_name, "wb") as file:
        file.write(r.content)
    
    return file_name


def main():
    download_cat()


if __name__ == "__main__":
    main()