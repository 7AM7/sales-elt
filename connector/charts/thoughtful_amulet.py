import pandas as pd
import plotly.graph_objects as go


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = go.Figure(
        go.Bar(
            x=df["total_sales_amount"], y=df["customer_id"], orientation="h", marker_color="skyblue"
        )
    )

    fig.update_layout(
        title_text="Total Sales Amount per Customer",
        xaxis_title="Total Sales Amount",
        yaxis_title="Customer Name",
        margin=dict(l=20, r=20, t=30, b=20),
    )

    return fig.to_html(full_html=False)
