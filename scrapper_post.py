import instaloader
from pystyle import *
import os 


os.system("cls")

banner = """
        ╦══╩══════════════0══════════════════╩══╦
               ┌─┐┌─┐┬─┐┌─┐┌─┐   ┌─┐┌─┐┌─┐┌┬┐
               └─┐│  ├┬┘├─┤├─┘───├─┘│ │└─┐ │ 
               └─┘└─┘┴└─┴ ┴┴     ┴  └─┘└─┘ ┴ 
        ╩══╦══════════════0══════════════════╦══╩
 ╔═════════╩═════════════════════════════════╩═════════╗
 """


def scrap_post(username):
	loader = instaloader.Instaloader()

	try:
		loader.download_profile(username, profile_pic_only=False)
		print(Colorate.Diagonal(Colors.red_to_yellow, f"[!] succesfuly scrap {username} post ! "))
	except Exception as e:
		print(Colorate.Diagonal(Colors.red_to_yellow, f"[!] Failed Scrap {username} post !"))

if __name__ == "__main__":
	print(Colorate.Diagonal(Colors.red_to_yellow, banner))
	pseudo = input(Colorate.Diagonal(Colors.red_to_yellow,"\n\n[?] Username : "))
	scrap_post(pseudo)