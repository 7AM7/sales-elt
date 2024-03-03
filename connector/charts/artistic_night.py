import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=df["quarter"],
            y=df["total_sales"],
            name="Total Sales",
            marker_color="rgb(55, 83, 109)",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df["quarter"],
            y=df["average_sale_amount"],
            name="Average Sale Amount",
            mode="lines+markers",
            line=dict(color="rgb(26, 118, 255)", width=2, dash="dot"),
            marker=dict(size=8),
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(
            x=df["quarter"],
            y=df["number_of_transactions"],
            name="Number of Transactions",
            mode="lines+markers",
            line=dict(color="rgb(255, 165, 0)", width=2),
            marker=dict(size=8),
        ),
        secondary_y=True,
    )

    fig.update_layout(
        title_text="Quarterly Sales Analysis",
        title_font_size=20,
        legend=dict(x=0.01, y=0.99, bordercolor="Black", borderwidth=1),
        font=dict(size=12),
    )

    fig.update_xaxes(title_text="Quarter", title_standoff=25, tickangle=-45, tickfont=dict(size=10))
    fig.update_yaxes(title_text="<b>Total Sales</b>", secondary_y=False, title_font=dict(size=14))
    fig.update_yaxes(
        title_text="<b>Average Sale Amount / Number of Transactions</b>",
        secondary_y=True,
        title_font=dict(size=14),
    )

    fig.update_traces(hoverinfo="text+name", hovertemplate=None)

    return fig.to_html(full_html=False)
