import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=df["month"], y=df["total_sales"], name="Total Sales"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df["month"],
            y=df["average_sale_amount"],
            name="Average Sale Amount",
            mode="lines+markers",
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(
            x=df["month"],
            y=df["number_of_transactions"],
            name="Number of Transactions",
            mode="lines+markers",
        ),
        secondary_y=True,
    )

    fig.update_xaxes(title_text="Month")

    fig.update_yaxes(title_text="Total Sales", secondary_y=False)
    fig.update_yaxes(title_text="Average Sale Amount / Number of Transactions", secondary_y=True)

    fig.update_layout(title_text="Monthly Sales Analysis")

    return fig.to_html(full_html=False)
