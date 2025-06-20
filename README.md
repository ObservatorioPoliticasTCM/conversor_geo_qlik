# Conversor Geo Qlik

Este repositório contém scripts para converter arquivos geográficos para formatos compatíveis com o Qlik.  
O script principal `shape-to-kml.py` converte arquivos de forma (shapefile, GeoJSON, etc.) para CSV, removendo a coluna de geometria e adicionando um identificador (`qlik_id`).

## Como usar

1. **Baixando o projeto**:

  - Para clonar o repositório via Git, execute:

    ```bash
    git clone https://github.com/ObservatorioPoliticasTCM/conversor_geo_qlik.git
    ```
    
  - Ou, para baixar o ZIP:
    
    - Acesse o repositório no GitHub.
    - Clique em "Code" e selecione "Download ZIP".

2. **Pré-requisitos**:  
   - Python 3.x instalado. 

- Crie um ambiente virtual (opcional, mas recomendado):

  No windows, use:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
  
  No linux, use:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

- Instale as bibliotecas necessárias utilizando o arquivo requirements.txt:
  
  ```bash
  pip install -r requirements.txt
  ```
   - Bibliotecas necessárias instaladas (por exemplo, geopandas).  

3. **Executando o Script**:

   No terminal, execute:

   ```bash
   python shape-to-kml.py <caminho_do_arquivo>
   ```

4. **Saída**:
    Após a execução, um arquivo KML e um arquivo CSV será gerado na mesma pasta do arquivo de entrada, com o mesmo nome base.
