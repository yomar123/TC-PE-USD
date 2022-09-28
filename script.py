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

# #Ver el contenido en bytes
# Cod_Bytes = response.content
# print(Cod_Bytes)
# print()

# #ver el contenido en cadena
# Cod_Text = response.text
# print(Cod_Text)
# print()

# #ver contenido  en codificacion explicita
# response.encoding = 'utf-8'
#Codific_Utf = response.text
# print(Codific_Utf )

#ver el contenido Json - Son diccionarios(Clave - Valor)
# Diccionariojson = response.json()
# print(Diccionariojson)
# print()
# print()

