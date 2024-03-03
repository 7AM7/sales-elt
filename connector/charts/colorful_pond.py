import pandas as pd
import plotly.graph_objects as go


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=df["product_id"].astype(str), y=df["likelihood_score"], marker_color="skyblue")
    )

    fig.update_layout(
        title="Likelihood of Products Being Ordered Again",
        xaxis_title="Product ID",
        yaxis_title="Likelihood Score",
        xaxis_tickangle=-45,
    )

    return fig.to_html(full_html=False)
