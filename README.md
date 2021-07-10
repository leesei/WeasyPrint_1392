[53.0b2 generate much larger PDF (and much slower) · Issue #1392 · Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint/issues/1392)

```sh
# setup venv (once only)
python -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt

# run program
./codes2tickets.py -vvvvv -o . ./schools.json

# `.html` and `.pdf` with 1000 tickets are generated
# `pip install weasyprint==53.0b2` to test new version
```
