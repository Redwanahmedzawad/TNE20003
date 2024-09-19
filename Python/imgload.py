import requests


def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True)as r:
        print("downloading")
        with open(local_filename,"wb") as f:
            print("writing to file")
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    f.close()
    print("downloaded")




download_files("http://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png")
