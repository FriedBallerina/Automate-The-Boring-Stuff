import pyperclip
userInput = input('Type anything you want to be copied to the Clipboard: ')
pyperclip.copy(userInput)
pyperclip.paste()
print("It's crazy but now what you have written has been copied and you can paste it wherever you need! :D")