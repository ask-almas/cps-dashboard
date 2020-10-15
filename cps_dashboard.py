from config.config import KAFKA_HOST, KAFKA_PORT, KAFKA_CONSUME_TOPICS
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from kafka_messages_counter import KafkaMessagesCounter


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H4(
        'Kafka Topic Messages'
    ),
    html.Table([
        html.Thead(
            html.Tr([html.Th(topic) for topic in KAFKA_CONSUME_TOPICS])
        ),
        html.Tbody(id='table-records')
    ]),
    dcc.Interval(
        id='interval-component',
        interval=1000,
        n_intervals=0
    )
])


@app.callback(Output('table-records', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_records(n):
    kmc = KafkaMessagesCounter(KAFKA_HOST, KAFKA_PORT, KAFKA_CONSUME_TOPICS)
    msgs = kmc.topics_messages_count()
    return [html.Tr(
        [html.Td(mas) for mas in msgs]
    )]


if __name__ == '__main__':
    app.run_server(debug=True)
