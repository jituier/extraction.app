from selenium import webdriver
from importlib_metadata import version
try:
    v0 = version('streamlit')
    v = v0.split(".")
    assert(int(v[1])>=10 or int(v[0])>1)
except:
    raise ImportWarning("This application needs version 1.10.0 or higher of Streamlit. Current version: "+v0)

# chargement du driver de Chrome
driver = webdriver.Chrome()


if __name__ == '__main__':
    import Accueil
    Accueil.main()
