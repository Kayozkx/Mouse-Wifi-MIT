from flask import Flask, request
import pyautogui

app = Flask(__name__)

# Segurança do PyAutoGUI

pyautogui.FAILSAFE = True


# TESTE DE CONEXÃO

@app.route('/ping')
def ping():
    return "ONLINE"


# MOVIMENTO DO MOUSE

@app.route('/move')
def move():

    try:
        dx = float(request.args.get('x', 0))
        dy = float(request.args.get('y', 0))

        # Ignora movimentos muito pequenos
        if abs(dx) < 1 and abs(dy) < 1:
            return "OK"

        sensibilidade = 5

        pyautogui.moveRel(
            int(dx * sensibilidade),
            int(dy * sensibilidade)
        )

        return "OK"

    except Exception as erro:
        print("ERRO MOVE:", erro)
        return str(erro), 500



# CLIQUE ESQUERDO

@app.route('/click')
def click():

    pyautogui.click()

    return "CLICK"



# CLIQUE DIREITO

@app.route('/rightclick')
def rightclick():

    pyautogui.rightClick()

    return "RIGHT"



# INICIAR SERVIDOR

if __name__ == '__main__':

    print("=" * 40)
    print("SERVIDOR MOUSE WIFI INICIADO")
    print("IP: veja com 'ipconfig' no terminal")
    print("PORTA: 5000")
    print("=" * 40)

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )
