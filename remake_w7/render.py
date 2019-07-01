from flask import Flask, render_template, request
import io

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    homework_list = list()

    ele1 = dict()
    ele1['homework_id'] = "1"
    ele1['about'] = "サンプルその1"

    ele2 = dict()
    ele2['homework_id'] = "2"
    ele2['about'] = "サンプルその2"

    homework_list.append(ele1)
    homework_list.append(ele2)

    return render_template("w7_04.html", homework_list=homework_list)


@app.route("/get_file", methods=['POST'])
def get_file():
    if 'uploadedFile' in request.files:
        print("get file")
    else:
        print("not get file")
        return "failed get file"

    # check file is selected
    uploaded_file = request.files['uploadedFile']
    if uploaded_file.filename == '':
        print("uploaded file is not selected")
        return "failed get file"

    uploaded_file.save("upload_folder")
    return "saved"


if __name__ == "__main__":
    app.run(debug=True)
    