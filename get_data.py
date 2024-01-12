from bs4 import BeautifulSoup

html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../projectForOnly/assest/styles/styles.css">
    <title>Регистрация и авторизация</title>
</head>
<body>
<div class="container">
    <form id="registrationForm" action="../projectForOnly/pages/register.php" method="post">
        <h2>Регистрация</h2>
        <label for="name">Имя:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="phone">Телефон:</label>
        <input type="tel" id="phone" name="phone" required>
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password" required>
        <label for="confirmPassword">Повторите пароль:</label>
        <input type="password" id="confirmPassword" name="confirmPassword" required>
        <button type="submit">Зарегистрироваться</button>
    </form>

    <form id="loginForm" action="../projectForOnly/pages/login.php" method="post">
        <h2>Авторизация</h2>
        <label for="login">Email или телефон:</label>
        <input type="text" id="login" name="login" required>
        <label for="loginPassword">Пароль:</label>
        <input type="password" id="loginPassword" name="loginPassword" required>

        <div
                id="captcha-container"
                class="smart-captcha"
                data-sitekey="<ключ_клиента>"
        ></div>


        <button type="submit">Войти</button>
    </form>
</div>

        <ol>
             <li>HTML test for Parse</li>
             <li id="css-li">HTML test for Parse</li>
             <li class="green">JS</li>
             <li class="green">Python</li>
        </ol>
        
<script src="script.js"></script>
<script src="https://smartcaptcha.yandexcloud.net/captcha.js" defer></script>

</body>
</html>
"""

# parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

# print(parsed_html.body.h2)

# print(parsed_html.find(id="loginPassword"))

# print(parsed_html.find_all(class_="container"))  незабудь что при поиске класса надо нижнее подкеркивание

parsed_html = BeautifulSoup(html_string, 'html.parser')

# print(parsed_html.select("li")[3])

html_elem = parsed_html.select("li")[3]
print(html_elem.get_text())