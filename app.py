from flask import Flask, render_template, request
import os  

app = Flask(__name__)


TAXA_STEAM = 0.15 

TAXA_CSFLOAT = 0.02

TAXA_BUFF_COMPRA = 0.09

@app.route('/', methods=['GET', 'POST'])
def index():
    
    resultados = {}

    if request.method == 'POST':
        try:

            preco_bruto_buff = float(request.form['custo_buff'])
            preco_steam = float(request.form['preco_steam'])
            preco_csfloat = float(request.form['preco_csfloat'])


            custo_buff = preco_bruto_buff * (1 + TAXA_BUFF_COMPRA)


            recebido_steam = preco_steam * (1.0 - TAXA_STEAM)
            recebido_csfloat = preco_csfloat * (1.0 - TAXA_CSFLOAT)


            lucro_steam = recebido_steam - custo_buff
            lucro_csfloat = recebido_csfloat - custo_buff


            resultados = {
                'lucro_steam': lucro_steam,
                'lucro_csfloat': lucro_csfloat
            }
        
        except ValueError:

            resultados = {'erro': 'Por favor, insira valores numéricos válidos.'}

        except Exception as e:
            resultados = {'erro': f'Ocorreu um erro: {e}'}


    return render_template('index.html', **resultados)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000)) 
    app.run(host='0.0.0.0', port=port, debug=False)
