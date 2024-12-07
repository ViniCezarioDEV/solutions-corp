from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
import os

LIST_MUSICS = []
STATUS_LIST = []
DOWNLOAD_DIR = 'solutions-corp/uploads'
downloaded_files = []

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def YTdownloader():
    if LIST_MUSICS:
        for music in LIST_MUSICS:
            if 'https://' in music:
                try:
                    ydl_opts = {
                        'format': 'bestaudio/best',  # Seleciona o melhor áudio disponível
                        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extrair o áudio
                            'preferredcodec': 'mp3',  # Converte para MP3
                            'preferredquality': '320',  # Qualidade do áudio (192 kbps neste caso)
                        }],
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(music, download=True)
                        downloaded_files.append(info_dict['title'] + '.mp3')
                    
                    STATUS_LIST.append(f"{music} SUCESSO.")
                    
                except Exception as e:
                    STATUS_LIST.append(f'{music} FALHOU. {e}')

            else:
                results = YoutubeSearch(music, max_results=1).to_dict()
                try:
                    url = 'youtube.com{}'.format(results[0]['url_suffix'])
                    ydl_opts = {
                        'format': 'bestaudio/best',  # Seleciona o melhor áudio disponível
                        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extrair o áudio
                            'preferredcodec': 'mp3',  # Converte para MP3
                            'preferredquality': '320',  # Qualidade do áudio (192 kbps neste caso)
                        }],
                    }
                    with YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(url, download=True)
                        downloaded_files.append(info_dict['title'] + '.mp3')
                    
                    STATUS_LIST.append(f"{music} SUCESSO.")
    
                except Exception as e:
                    STATUS_LIST.append(f'{music} FALHOU. {e}')
        return downloaded_files  # Retorna os arquivos baixados
        
    else:
        STATUS_LIST.append(f'A lista de músicas está vazia!')