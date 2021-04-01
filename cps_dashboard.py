import time
import dash
import utm
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash_extensions import Keyboard

from config.config import SYMBOLS, OPACITY, COLORS, SIZES, MAPBOX_TOKEN
from kafka_client import KafkaClient
from object_lists_thread import ObjectListsThread
from topic_object import TopicObject

app = dash.Dash()
obj_idx = 0
old_topic = None
obj_list = None

workers = {"detections": None,
           "detections-utm": None,
           "objects-utm": None,
           "fusion-utm": None,
           "objects": None,
           "campus-st": None}

obj_lists = {"detections": TopicObject("detections"),
             "detections-utm": TopicObject("detections-utm"),
             "objects-utm": TopicObject("objects-utm"),
             "fusion-utm": TopicObject("fusion-utm"),
             "objects": TopicObject("objects"),
             "campus-st": TopicObject("campus-st")}

app.layout = html.Div(children=[Keyboard(id="keyboard"),
                                html.H1("Central Perception Dashboard"),
                                dcc.Dropdown(id="topic-choice"),
                                dcc.Interval(id='interval_component', interval=1000, n_intervals=0),
                                html.Div(id="output"),
                                dcc.Graph(id="bev_map", animate=False)
                                ]
                      )


@app.callback(Output('topic-choice', 'options'),
              Input('interval_component', 'n_intervals'))
def update_options(n):
    kafka_client = KafkaClient()
    return kafka_client.get_topic_options()


@app.callback([Output("output", "children"),
               Output('bev_map', 'figure')],
              [Input("keyboard", "keydown"),
               Input("keyboard", "n_keydowns"),
               Input("topic-choice", "value")])
def keydown(event, n_keydowns, value):
    global obj_list, obj_idx, old_topic, obj_lists

    if value is None:
        scene = get_curr_scene()
        return scene

    if value != old_topic:
        old_topic = value
        obj_idx = 0
        if workers[value] is None:
            print("Worker Not Found")
            x = ObjectListsThread(obj_lists[value])
            print("Creating Thread")
            x.start()
            workers[value] = x
            time.sleep(1)
            print("Retrieving Messages from Kafka")
            obj_list = obj_lists[value]
        else:
            print(f"Number of scenes={len(obj_list)}")
            obj_list = obj_lists[value]
        scene = get_curr_scene(obj_list.is_utm())
        print("done")
        return scene

    if event is not None and event["key"] == "ArrowRight":
        if obj_idx < len(obj_list) - 1:
            obj_idx += 1
    if event is not None and event["key"] == "ArrowLeft":
        if obj_idx > 0:
            obj_idx -= 1

    scene = get_curr_scene(obj_list.is_utm())
    return scene


def get_curr_scene(is_utm=False):
    global obj_list, obj_idx, old_topic
    scene_objects = obj_list.get_by_index(obj_idx) if obj_list else []
    # TODO: maybe somehow it can be avoided to create new figure object for each step
    fig = go.Figure()
    fig.add_trace(go.Scattermapbox())
    fig.update_layout(showlegend=True,
                      autosize=False,
                      width=1000,
                      height=600,
                      mapbox=dict(style='outdoors',
                                  accesstoken=MAPBOX_TOKEN,
                                  zoom=18,
                                  center={"lat": 47.47894534674124,
                                          "lon": 19.056331847185383}))

    if len(scene_objects) > 0 and scene_objects[-1] is not None:
        data_sources = {}
        origins = []
        for so in scene_objects:
            if so.ssid not in data_sources:
                data_sources[so.ssid] = []
                origins.append(so)
            if so.suid >= 0:
                data_sources[so.ssid].append(so)

        object_nums = {}
        for source_system in data_sources:
            ds_objects = data_sources[source_system]
            object_nums[source_system] = len(ds_objects)

        for orig in origins:
            fig.add_trace(go.Scattermapbox(
                lon=[utm.to_latlon(orig.lon, orig.lat, 34, 'U')[1] if is_utm else orig.lon],
                lat=[utm.to_latlon(orig.lon, orig.lat, 34, 'U')[0] if is_utm else orig.lat],
                marker=dict(
                    color='brown',
                    size=15,
                    symbol='star'
                ),
                text=f"source system: {orig.ssid}",
                name=f"source system: {orig.ssid}"
            ))

        for source_system in data_sources:
            ds_objects = data_sources[source_system]
            fig.add_trace(go.Scattermapbox(
                lon=[utm.to_latlon(o.lon, o.lat, 34, 'U')[1] if is_utm else o.lon for o in ds_objects],
                lat=[utm.to_latlon(o.lon, o.lat, 34, 'U')[0] if is_utm else o.lat for o in ds_objects],
                marker=dict(
                    color=COLORS[source_system],
                    size=SIZES[source_system],
                    symbol=SYMBOLS[source_system]
                    ),
                opacity=OPACITY[source_system],
                mode="markers",
                text=[f"{o.cov_xx:.3f}     {o.cov_yy:.3f}" for o in ds_objects] if source_system != "3_390" else "",
                name=f"{source_system}: {object_nums[source_system]} detected objects",
            ))
        return f"Fusion time @ {scene_objects[-1].ts / 1000.0}", fig
    else:
        return f"No data in future! (requested fusion step: {obj_idx})", fig


if __name__ == '__main__':
    app.run_server(debug=True)
