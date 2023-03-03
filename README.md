# parser-vendor-code
Проект для разбора номеров гидроцилиндров

## Install

```commandline
pip install -r requirements.txt
```

## Run
```commandline
python ParserVendorCode.py
```


## Build exe
```commandline
pyinstaller --onefile --windowed  --name "ParserVendorCode"  --noconsole -y ParserVendorCode.py
```