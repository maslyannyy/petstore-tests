Install deps
```bash
pip install -r requirements.txt
```

Run tests
```bash
rm -rf ./results
py.test --alluredir=./results
```

Watch results
```bash
allure serve ./results
```