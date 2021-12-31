import sys
print(f"Work with {sys.version}")
# clbe0xae23@cashflow35.com
# iu11miori1q84ubzp0o28j73qp99v2gxy55vw9p7yu1jrm58n4t3mkofa003
from fastapi import FastAPI
from app import main
app = FastAPI()
main.main(app)

