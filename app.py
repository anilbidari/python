from flask import Flask,request,jsonify;
from datetime import datetime;
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<head>
   <title>My title</title>
</head>
<body style="width: 880px; margin: auto;">  


<pre>


   ____   _                       _     _____                   _       _              _ 
  / ___| | |   ___    _   _    __| |   | ____|  _ __     __ _  | |__   | |   ___    __| |
 | |     | |  / _ \  | | | |  / _` |   |  _|   | '_ \   / _` | | '_ \  | |  / _ \  / _` |
 | |___  | | | (_) | | |_| | | (_| |   | |___  | | | | | (_| | | |_) | | | |  __/ | (_| |
  \____| |_|  \___/   \__,_|  \__,_|   |_____| |_| |_|  \__,_| |_.__/  |_|  \___|  \__,_|
                                                                                         

</pre>

    <h1>A Python Flask API</h1>

    <img src="http://thecloudenabled.com/wp-content/uploads/2017/04/xlogo1-1.png.pagespeed.ic.12uoJYChtw.png">

    <h3>Want JSON? go to <a href="/hello?user=yourname" target="_blank">/hello?user=yourname</a></h3> 

<pre>
 
 __        __         _                                       _               ____   __   __    _____   _                 _      _ 
 \ \      / /   ___  | |   ___    ___    _ __ ___     ___    | |_    ___     |  _ \  \ \ / /   |  ___| | |   __ _   ___  | | __ | |
  \ \ /\ / /   / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \    | |_) |  \ V /    | |_    | |  / _` | / __| | |/ / | |
   \ V  V /   |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |   |  __/    | |     |  _|   | | | (_| | \__ \ |   <  |_|
    \_/\_/     \___| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/    |_|       |_|     |_|     |_|  \__,_| |___/ |_|\_\ (_)
                                                                                                                                   

</pre>                                                                                       

</body>
"""

@app.route('/hello')
def get_current_user():
    now = datetime.now()
    return jsonify(
        user = request.args.get('user'),
        time = now
    )

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)