#!/usr/bin/python3

import tweepy
import sys
import random

# Twitter API Keys
CK = ""
CS = ""
AT = ""
AS = ""

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#名前のリスト
l = [
    "desktop",
    "xlsx",
    "gif",
    "jpeg",
    "js",
    "bin",
    "com",
    "mkv",
    "exe",
    "obj",
    "rpm",
    "clip",
    "apk",
    "aui",
    "lang",
    "hlp",
    "mp3",
    "pac",
    "aac",
    "rv",
    "rb",
    "DS_Store",
    "pdf",
    "xz",
    "iso",
    "mcpack",
    "shtml",
    "meta",
    "odc",
    "tra",
    "apks",
    "odp",
    "so",
    "webm",
    "7z",
    "kext",
    "txt",
    "xls",
    "deb",
    "doc",
    "aml",
    "dvr-ms",
    "html",
    "win",
    "aup",
    "tar",
    "pck",
    "ps1",
    "java",
    "blend",
    "tmp",
    "Z",
    "midi",
    "proj",
    "wma",
    "msi",
    "ymmp",
    "bz",
    "jxw",
    "csv",
    "sys",
    "cs",
    "htm",
    "bat",
    "pptx",
    "plist",
    "nsk",
    "sln",
    "xapk",
    "odg",
    "nds",
    "obb",
    "old",
    "auf",
    "gz",
    "ra",
    "sh",
    "rar",
    "m4a",
    "aiff",
    "psd",
    "mpg",
    "asp",
    "rm",
    "rel",
    "lzh",
    "otf",
    "zip",
    "mpeg",
    "scr",
    "auc",
    "org",
    "lock",
    "json",
    "wncry",
    "tja",
    "jpg",
    "wmv",
    "mobileconfig",
    "wav",
    "webp",
    "url",
    "car",
    "mcworld",
    "wm",
    "jar",
    "bmp",
    "scala",
    "cfg",
    "config",
    "ico",
    "png",
    "mcmeta",
    "flac",
    "dat",
    "lwi",
    "cab",
    "php",
    "ipa",
    "qt",
    "swf",
    "reg",
    "xml",
    "anm",
    "ppt",
    "mht",
    "cpp",
    "app",
    "cap",
    "avi",
    "dic",
    "yaml",
    "jpe",
    "sawnd",
    "jfif",
    "ttf",
    "rtf",
    "asc",
    "odt",
    "asset",
    "opus",
    "md",
    "dib",
    "cgi",
    "auo",
    "wmf",
    "lua",
    "exo",
    "h",
    "docx",
    "tiff",
    "log",
    "c",
    "mid",
    "mov",
    "chm",
    "ani",
    "py",
    "pyw",
    "mp4",
    "crdownload",
    "class",
    "css",
    "dll",
    "bak",
    "cur",
    "gpg",
    "piv",
    "dsv",
    "sjis",
    "docs",
]

def main():
    
    #TwitterAPIで名前を取得する
    me = api.me()

    #取得した名前を出力する
    print(me.name)

    #randomモジュールを使い、名前を辞書からランダムに選ぶ
    choice_num = random.randint(1, len(l))
    choice = l[choice_num]

    #name変数に変更予定の名前を代入する
    name = f"おなまえ.{choice}"

    #名前を出力する
    print(f"名前を{me.name}から{name}に変更しました。")
    
    #TwitterAPIを使い、名前を変更する
    api.update_profile(name)

    #変更通知をツイートする
    api.update_status(f"名前を{me.name}から{name}に変更しました。")


if __name__ == "__main__":
    main()
