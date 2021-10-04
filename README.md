[Performance issue on v53 with large font · Issue #1457 · Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint/issues/1457) v53 is much slower

~~[53.0b2 generate much larger PDF (and much slower) · Issue #1392 · Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint/issues/1392)~~ file size fixed

```sh
# setup venv (once only)
python -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt

# run program
./codes2tickets.py -vvvvv -o . ./schools.json

# `.html` and `.pdf` with 1000 tickets are generated
# `pip install weasyprint==52.5` to test old version
```
