from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# New working Thirukkural API
API_URL = "https://tamil-kural-api.vercel.app/api/kural/{}"


@app.route("/", methods=["GET", "POST"])
def home():

    kural = None
    error = None

    if request.method == "POST":

        number = request.form.get("number", "").strip()

        # Check empty input
        if not number:
            error = "Please enter a Kural number."

        # Check number
        elif not number.isdigit():
            error = "Please enter a valid number."

        elif int(number) < 1 or int(number) > 1330:
            error = "Please enter a number between 1 and 1330."

        else:

            try:
                # Create API URL
                url = API_URL.format(number)

                # Call API
                response = requests.get(url, timeout=10)

                # Check response
                if response.status_code == 200:

                    data = response.json()

                    kural = {
                        "number": data.get("number"),
                        "chapter": data.get("chapter"),
                        "section": data.get("section"),
                        "line1": data.get("kural", ["", ""])[0],
                        "line2": data.get("kural", ["", ""])[1],
                        "tamil_meaning": data.get("meaning", {}).get("ta_mu_va", ""),
                        "english_meaning": data.get("meaning", {}).get("en", "")
                    }

                else:
                    error = f"API error: {response.status_code}"

            except requests.exceptions.RequestException:
                error = "Unable to connect to the Thirukkural API."

            except Exception as e:
                error = "Something went wrong."


    return render_template(
        "index.html",
        kural=kural,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)