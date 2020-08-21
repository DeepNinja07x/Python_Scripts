import os
import instaloader

def pic_download(name):
    parser=instaloader.Instaloader()
    os.chdir(os.path.join(os.path.expanduser('~'),'Downloads'))

    if os.path.isdir("Insta Downloads"):
        os.chdir("Insta Downloads")
        return parser.download_profile(name, profile_pic_only=True)
    else:
        os.mkdir("Insta Downloads")
        os.chdir("Insta Downloads")
        return parser.download_profile(name, profile_pic_only=True)

if __name__=="__main__":
    user=input("Enter the Username: ")
    pic_download(user)
        
