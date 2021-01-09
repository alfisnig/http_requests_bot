import requests


def http_get_request_to_txt(url: str, file_name: str):
    """ВОзвращает текстовый файл (объект) в ответ на get запрос"""
    text = get_request_text(url)
    write_response_to_txt(text, file_name)
    file = open_txt_with_response(file_name)
    return file

def get_request_text(url: str):
    """Получение html кода страницы"""
    request = requests.get(url)
    html_code = request.text
    return html_code

def write_response_to_txt(response: str, file_name):
    """Записывает html код страницы запроса в .txt файл"""
    with open(file_name, "w", encoding="UTF-8") as response_file:
        response_file.write(response)

def open_txt_with_response(file_name: str):
    """Откроывает txt файл (в бинарном виде) с html кодом страницы"""
    response_file = open(file_name, "rb")
    return response_file, file_name
