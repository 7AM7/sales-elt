import pandas as pd
import plotly.express as px


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = px.bar(
        df,
        x="rank",
        y="total_sales",
        text="customer_id",
        title="Total Sales by Customer Rank",
        labels={"total_sales": "Total Sales", "rank": "Customer Rank"},
        orientation="v",
    )

    fig.update_traces(marker_color="skyblue", textposition="outside", hoverinfo="text+y")

    fig.update_layout(
        xaxis_tickmode="linear",
        xaxis_title="Customer Rank",
        yaxis_title="Total Sales",
        hovermode="x unified",
    )

    return fig.to_html(full_html=False)
