from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_data = file.read()

        md5_hash = hashlib.md5(file_data, usedforsecurity=False).hexdigest()
        sha1_hash = hashlib.sha1(file_data, usedforsecurity=False).hexdigest()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
        sha384_hash = hashlib.sha384(file_data).hexdigest()
        sha512_hash = hashlib.sha512(file_data).hexdigest()
        sha3_256_hash = hashlib.sha3_256(file_data).hexdigest()
        blake2b_hash = hashlib.blake2b(file_data).hexdigest()
        blake2s_hash = hashlib.blake2s(file_data).hexdigest()

        return render_template('results.html', md5_hash=md5_hash,
                               sha1_hash=sha1_hash, sha256_hash=sha256_hash,
                               sha384_hash=sha384_hash, sha512_hash=sha512_hash,
                               sha3_256_hash=sha3_256_hash, blake2b_hash=blake2b_hash,
                               blake2s_hash=blake2s_hash)

    return render_template('hashfinder.html')

if __name__ == '__main__':
    app.run(debug=False)
