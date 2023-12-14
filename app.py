from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    try:
        input_text = request.form[
       
'input_text']
        response = requests.get(f'https://pyrubi.b80.xyz/G4.php?text={input_text}')
        if response.status_code == 200:
            result = response.json()["result"]
            # return result
            req = requests.get(f"https://pyrubi.b80.xyz/chat.php/?text={input_text}").json()
            res = req[0]["text"]
            return res+'\n'
        
            
        else:
            return "Failed to retrieve data"
    except Exception as e:
        return f"An error occurred: {e}"
    
    
    

if __name__ == '__main__':
    app.run(debug=True)
    # https://bot.writesonic.com/?workspace_id=5796a525-9431-482b-a0f0-906fd63e72f5
    
    
    