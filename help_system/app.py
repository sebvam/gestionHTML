import os, sys, configparser, webview, xml.etree.ElementTree as ET

BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

def load_ini(path):
    cfg = configparser.ConfigParser()
    cfg.read(path, encoding='utf-8')
    return cfg

def load_xml(path):
    tree = ET.parse(path)
    return tree.getroot()

INI_PATH = os.path.join(BASE_DIR, "config", "config.ini")
XML_PATH = os.path.join(BASE_DIR, "config", "config.xml")
INDEX_HTML = os.path.join(BASE_DIR, "templates", "index.html")

def main():
    if os.path.exists(INI_PATH):
        cfg = load_ini(INI_PATH)
        title = cfg.get('window','title', fallback='Sistema de Ayuda')
        width = cfg.getint('window','width', fallback=1024)
        height = cfg.getint('window','height', fallback=768)
        start_page = cfg.get('app','start_page', fallback=INDEX_HTML)
        if not os.path.isabs(start_page):
            start_page = os.path.join(BASE_DIR, start_page)
    else:
        title, width, height, start_page = 'Sistema de Ayuda', 1024, 768, INDEX_HTML

    xml_root = None
    if os.path.exists(XML_PATH):
        xml_root = load_xml(XML_PATH)

    start_url = 'file:///' + os.path.abspath(start_page).replace('\\','/')
    window = webview.create_window(title, start_url, width=width, height=height)
    webview.start()

if __name__ == "__main__":
    main()
