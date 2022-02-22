import osmnx as ox


def draw_map(lat, long, label, draw_distance=5000):
    point = (lat, long)
    G = ox.graph_from_point(point, dist=draw_distance, retain_all=True, simplify=True, network_type='drive')
    u = []
    v = []
    key = []
    data = []
    for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
        u.append(uu)
        v.append(vv)
        key.append(kkey)
        data.append(ddata)
    road_colors = []
    road_widths = []
    for item in data:
        if "length" in item.keys():
            if item["length"] <= 100:
                linewidth = 0.90
                color = "#11999E"

            elif item["length"] > 100 and item["length"] <= 200:
                linewidth = 0.76
                color = "#11999E"

            elif item["length"] > 200 and item["length"] <= 350:
                linewidth = 1.10
                color = "#11999E"

            elif item["length"] > 350:
                color = "#D8D860"
                linewidth = 3.75
            else:
                color = "#888888"
                linewidth = 0.95
        else:
            color = "#A0AECD"
            linewidth = 0.10

        road_colors.append(color)
        road_widths.append(linewidth)

    bgcolor = "#1D5464"
    fig, ax = ox.plot_graph(G, node_size=0, figsize=(27, 40),
                            dpi=200, bgcolor=bgcolor,
                            save=False, edge_color=road_colors,
                            edge_linewidth=road_widths, edge_alpha=1)
    ax.set_title(label, fontdict=
    {'fontsize': '60',
     'color': '#D8D860',
     'verticalalignment': 'center',
     'horizontalalignment': 'center'}
                 )
    fig.tight_layout(pad=0)
    fig.savefig("map.png", dpi=200, bbox_inches='tight', format="png", facecolor=fig.get_facecolor(), transparent=False)


draw_map(43.466667, -80.516670,'Waterloo driving roads', 13000)
