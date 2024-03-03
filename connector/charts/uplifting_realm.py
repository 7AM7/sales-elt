import pandas as pd
import plotly.graph_objects as go


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = go.Figure(go.Bar(x=df["product_id"], y=df["average_quantity"], marker_color="skyblue"))

    # Set titles and labels
    fig.update_layout(
        title_text="Average Order Quantity per Product",
        xaxis_title="Product ID",
        yaxis_title="Average Quantity",
        xaxis_tickangle=-45,
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="white",
    )
    return fig.to_html(full_html=False)
