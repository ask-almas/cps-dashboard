import time

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash_extensions import Keyboard

from config.config import SYMBOLS, OPACITY, COLORS, SIZES
from kafka_client import KafkaClient
from flask_caching import Cache

app = dash.Dash()
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
TIMEOUT = 600
obj_list = [[]]
obj_idx = 0
old_topic = None

app.layout = html.Div(children=[
    Keyboard(id="keyboard"),
    html.H1("Central Perception Dashboard"),
    dcc.Dropdown(id="topic-choice"),
    dcc.Interval(id='interval_component', interval=1000, n_intervals=0),
    html.Div(id="output"),
    dcc.Graph(id="bev_map", animate=False)
])


@app.callback(Output('topic-choice', 'options'), Input('interval_component', 'n_intervals'))
def update_options(n):
    kafka_client = KafkaClient()
    return kafka_client.get_topic_options()


@app.callback([Output("output", "children"), Output('bev_map', 'figure')],
              [Input("keyboard", "keydown"), Input("keyboard", "n_keydowns"), Input("topic-choice", "value")])
def keydown(event, n_keydowns, value):
    global obj_list, obj_idx, old_topic

    if value is None:
        scene = get_curr_scene()
        return scene

    is_utm = False
    if 'utm' in value:
        is_utm = True

    is_detection = False
    if 'detection' in value:
        is_detection = True

    if value != old_topic:
        old_topic = value
        obj_idx = 0
        obj_list = [[]]
        obj_list = update_obj_list(value, is_utm, is_detection)
        scene = get_curr_scene(is_utm)
        print("done")
        return scene

    if event is not None and event["key"] == "ArrowRight":
        if obj_idx < len(obj_list) - 1:
            obj_idx += 1
    if event is not None and event["key"] == "ArrowLeft":
        if obj_idx > 0:
            obj_idx -= 1

    scene = get_curr_scene(is_utm)
    return scene


@cache.memoize(timeout=TIMEOUT)
def update_obj_list(value, is_utm=False, is_detection=False):
    kafka_client = KafkaClient()
    return kafka_client.get_messages_from_topic(value, is_utm, is_detection)


def get_curr_scene(is_utm=False):
    global obj_list, obj_idx
    scene_objects = obj_list[obj_idx]
    # TODO: maybe somehow it can be avoided to create new figure object for each step
    fig = go.Figure()
    fig.update_layout(
        showlegend=True,
        autosize=False,
        width=900,
        height=900
    )

    if not is_utm:
        fig.update_xaxes(range=[19.05583, 19.05697])
        fig.update_yaxes(range=[47.47845, 47.47925])
    else:
        fig.update_xaxes(range=[353520.38, 353608.49])
        fig.update_yaxes(range=[5260166.73, 5260253.49])

    if len(scene_objects) > 0 and scene_objects[-1] is not None:
        data_sources = {}
        for so in scene_objects:
            if so.ssid not in data_sources:
                data_sources[so.ssid] = []
            if so.suid >= 0:
                data_sources[so.ssid].append(so)
        for source_system in data_sources:
            ds_objects = data_sources[source_system]
            fig.add_trace(go.Scatter(
                x=[o.lon for o in ds_objects],
                y=[o.lat for o in ds_objects],
                marker=dict(color=COLORS[source_system], size=SIZES[source_system]),
                opacity=OPACITY[source_system],
                mode="markers+text",
                text=[f"{o.cov_xx:.3f}     {o.cov_yy:.3f}" for o in ds_objects] if source_system != "3_390" else "",
                marker_symbol=SYMBOLS[source_system],
                name=source_system
            ))
        object_nums = {}
        for source_system in data_sources:
            ds_objects = data_sources[source_system]
            object_nums[source_system] = len(ds_objects)
        return f"{old_topic} Fusion time @ {scene_objects[-1].ts / 1000.0} {object_nums}", fig
    else:
        return f"No data in future! (requested fusion step: {obj_idx})", fig


if __name__ == '__main__':
    app.run_server(debug=True)
