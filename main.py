import threading
import webview
import youtube_dl as yt
import webview

class API:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def dw(self, url):
        print(url)
        ydl_opts = {}
        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        response = {
            "message" : "Downloading completed."
        }
        return response

if __name__ == '__main__':
    api = API()
    window = webview.create_window('YTDownloader', 'web\index.html', js_api=api)
    webview.start(debug=True)
