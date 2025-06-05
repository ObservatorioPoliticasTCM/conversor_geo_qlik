from geopandas import GeoDataFrame
import os
import geopandas as gpd
import sys

def gdf_to_qlik(gdf:GeoDataFrame,
                filename:str,
                order_by:str=None) -> None:
    if not order_by:
        order_by = gdf.columns[0]

    print(f"Salvando o kml em {filename}.kml")
    (
        gdf
        .sort_values(order_by)
        .to_crs('wgs84')
        .to_file(f'{filename}.kml',
                 driver='KML',
                 index=False)
    )

    print(f"Salvando o csv em {filename}.csv")
    qlik_id = [f'p{i}' for i in range(1, gdf.shape[0]+1)]
    (
        gdf
        .sort_values(order_by)
        .drop(columns='geometry')
        .assign(qlik_id= qlik_id)
        .to_csv(f'{filename}.csv',
                 index=False)
    )



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python shape-to-kml.py <caminho_do_arquivo>")
        sys.exit(1)
    input_path = sys.argv[1]

    gdf = gpd.read_file(input_path)

    base_name = os.path.splitext(input_path)[0]

    gdf_to_qlik(gdf, base_name)