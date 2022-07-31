# htmlとの値の受け渡しのため、render_templateとrequestを追加でインポート
from flask import Flask, redirect, render_template, request, url_for

from database  import insert_ai_analysis_log
from rest_api import post_api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/send_request", methods=["post"])
def send_request():
    image_path = request.form.get("image_path")
    try:
        response, request_timestamp, response_timestamp = post_api(image_path)
    except:
        return render_template('false.html',image_path=image_path,message="API Connection Error")
        
    if response.get("success")==True:
        try:
            sql = insert_ai_analysis_log(
                image_path=image_path, 
                success=response.get("success"), 
                message=response.get("message"),
                estimated_class=response.get("estimated_data").get("class"), 
                confidence=response.get("estimated_data").get("confidence"),
                request_timestamp=request_timestamp, 
                response_timestamp=response_timestamp
            )
        except:
            return render_template('false.html',image_path=image_path,message="Failed to register to database")

        return render_template('success.html',sql=sql,image_path=image_path,response=response)
    else:
        return render_template('false.html',image_path=image_path,message=response)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/false")
def false():
    return render_template('false.html')

if __name__ == "__main__":
    app.run()