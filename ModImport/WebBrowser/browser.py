import webbrowser

# webbrowser.open('https://python.org/', new=1)
#
# help(webbrowser)
chrome = webbrowser.get(using='WindowsDefault')
chrome.open_new('https://python.org/')
