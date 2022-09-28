import requests

print("Hello, World")
print()
print()

# url = "https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioContable.aspx"

url2 = 'https://api.github.com'


response = requests.get(url2)

if response.status_code == 200:
    print("Success!")
else:
    print("An error has occurred.")

