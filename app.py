import os
import datetime
import sys
sys.path.append('backend')
import katudon
import takoyaki
from flask import Flask, render_template, request, redirect ,send_from_directory

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('home.html')

@app.route('/crop',methods=["GET"])
def cropping():
    return render_template('cropping.html')

@app.route('/crop',methods=["POST"])
def upload():
    #p = request.form.get('file')
    p = request.files["file"]
    if p is not None:
        print("fileが送られました")
        timestamp = str (datetime.datetime.now())
        timestamp
        @app.route('/kansei/<timestamp>')
        def kansei(timestamp):
	    #なんかの処理
            if (not os.dir_exist(os.path.join(app.root_path, f"data/{timestamp}"))):
                return 'url間違ってるよ'
            else if (os.file_exist(f"~~~/{timestamp}/{timestamp}.gif")):
            # 存在する場合
            # 完成済のページを返す
                return # ページのtemplateに変数を埋め込み
            else:
                return render_template('wait.html')v 0ujhjhcvvv
	
画像受信
    else:
        print("うまくいっていません")
    return redirect("/")

@app.route('/pray')
def praying():
    return render_template('pray.html')



## おまじない
if __name__ == "__main__":
    app.run(debug=True)

